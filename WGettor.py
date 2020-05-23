#! /usr/bin/python3
# rootVIII
from threading import Thread, Lock
from argparse import ArgumentParser
from os import popen
from subprocess import call, Popen, PIPE
from random import randint
from sys import exit
# run with sudo privileges:
# sudo python -t https://somesite.com -n 1000
#
# Tested on Ubuntu 16. Intended for Debian Systems
#
# Tor must be installed and running as a service
# on localhost at port 9050
#
# This program relies on the Torsocks shell utility
#
# requirements: Python3, Tor/Torsocks, netstat, wget


class WgetTor:
    def __init__(self, target_address, number):
        self.target_address = target_address
        self.number_requests = int(number)
        self.reload = 'service tor reload'
        self.wget = "torsocks wget -q --spider --user-agent='%s' %s"
        self.lock = Lock()
        self.user_agents = self.set_user_agents()

    # replace or add additional user agents here
    @staticmethod
    def set_user_agents():
        return [
            "Opera/9.80 (S60; SymbOS; Opera Mobi/498; U; sv)",
            "Wget/1.11.4 (Red Hat modified)",
            "GSiteCrawler/v1.06 rev. 251 (http://gsitecrawler.com/)",
            "Mozilla/2.02 [fr] (WinNT; I)",
            "WeatherReport/1.2.2 CFNetwork/485.12.7 Darwin/10.4.0",
            "W3C_Validator/1.432.2.10",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)",
            "Cyberdog/2.0 (Macintosh; 68k)",
            "MJ12bot/v1.0.8 (http://majestic12.co.uk/bot.php?+)",
            "Exabot/2.0",
            "TurnitinBot/1.5 (http://www.turnitin.com/robot/crawlerinfo.html)",
            "Jyxobot/1",
            "Mozilla/5.0 (compatible; news bot /2.1)",
            "admantx-sap/2.4 (+http://www.admantx.com/service-fetcher.html)",
            "curl/7.19.6 (i686-pc-cygwin)",
            "facebookexternalhit/1.1;line-poker/1.0",
            "ConveraCrawler/0.4",
            "Mozilla/4.0 (MSIE 6.0; Windows NT 5.1; Search)",
            "Yahoo Pipes 1.0",
            "EARTHCOM.info/1.6 [www.earthcom.info]",
            "librabot/1.0 (+http://search.msn.com/msnbot.htm)",
            "NetResearchServer/2.5(loopimprovements.com/robot.html)",
            "PHP/5.2.10",
            "msnbot-Products/1.0 (+http://search.msn.com/msnbot.htm)",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1;)"
        ]

    @staticmethod
    def whoami():
        who = ['whoami']
        return 'root' in Popen(who, stdout=PIPE).communicate()[0].decode()

    @staticmethod
    def check_listening():
        for line in popen('netstat -na --tcp'):
            if '127.0.0.1:9050' in line:
                return True
        return False

    def reload_tor(self):
        with self.lock:
            try:
                call(self.reload, shell=True)
            except Exception:
                pass

    def service_status(self):
        for line in popen('service --status-all'):
            yield line.split()

    def check_services(self):
        for i in self.service_status():
            if '+' in i and 'tor' in i:
                return True
        return False

    def check_config(self):
        if not self.whoami():
            error = "Please run wgettor.py with root privileges"
            print(error)
            exit(1)
        if not self.check_listening() or not self.check_services():
            error = 'Please ensure the Tor service is started '
            error += 'and listening on socket 127.0.0.1:9050'
            print(error)
            exit(1)

    def get_agent(self):
        return self.user_agents[randint(0, len(self.user_agents) - 1)]

    def request(self):
        cmd = self.wget % (self.get_agent(), self.target_address)
        try:
            Popen(cmd, stdout=PIPE, shell=True)
            stdout.write(cmd + '\r')
            stdout.write("\033[K")
        except Exception:
            pass
        finally:
            self.reload_tor()

    def run(self):
        for get in range(self.number_requests):
            t = Thread(target=self.request)
            t.start()


if __name__ == '__main__':
    description = 'Usage: python wgettor.py -t <target URL or IP> '
    description += '-n <number of requests to make on target>'
    parser = ArgumentParser(description=description)
    h = ('target URL or IP', 'number of requests')
    parser.add_argument('-t', '--target', required=True, help=h[0])
    parser.add_argument('-n', '--number', required=True, help=h[1])
    args_in = parser.parse_args()
    wgettor = WgetTor(args_in.target, args_in.number)
    wgettor.check_config()
    wgettor.run()
