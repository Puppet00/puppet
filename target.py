import socket
import time
import sys

class Target():
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def check(self):
        print("\033[94m Checking target\033[0m")
        time.sleep(1)
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((self.host,int(self.port)))
            s.settimeout(1)
        except socket.error as e:
            print("\033[91m y", self.host, ":", self.port, "is an invalid target! \033[0m")
            sys.exit()
