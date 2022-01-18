import pyotp
import os
import time
import subprocess
#######
#PRİNT#
#######
os.system("pip install pyotp")
os.system("pip3 install pyotp")
print(" ")
print("\033[90m----------------------------CloudFlareDDoS--------------------------------- \033[0m")
print("\033[91m   ________________  ____  ____  ____ _  ___  __                            \033[0m")
print("\033[92m  / ____/ ____/ __ )/ __ \/ __ \/ __ | |/ \ \/ /                            \033[0m")
print("\033[93m / /   / /_  / __  / /_/ / /_/ / / / |   / \  /                             \033[0m")
print("\033[94m/ /___/ __/ / /_/ / ____/ _, _/ /_/ /   |  / /                              \033[0m")
print("\033[95m\____/_/   /_____/_/   /_/ |_|\____/_/|_| /_/                               \033[0m")
print("\033[96m----------------------------CloudFlareDDoS--------------------------------- \033[0m")
print(" ")
class LowkeyTWO_FactorAUTH:
    def __init__(self, sleutel, programma):
        self.key_pyotp = sleutel
        self.prog = programma
        self.live = pyotp.TOTP(f"{sleutel}")
    def twofactor_code(self):
        
        print(f"""
[ LowkeyPanel 2FA Authentication ]

> Your key is: 
\033[32m{self.key_pyotp}\033[0m

> Code For: 
\033[32m{self.prog}\033[0m   

> Live Time Code:
\033[32m{self.live.now()}\033[0m  

[INFO]
Automatic Renewing This Screen in 10 seconds...
""")
        time.sleep(10)
        subprocess.run("clear", shell=True, stderr=subprocess.DEVNULL)
        subprocess.run("cls", shell=True, stderr=subprocess.DEVNULL)
        twofa.twofactor_code()

twofa = LowkeyTWO_FactorAUTH('JBSWY3DPXHPK3PXP','LowkeyCLI Auth')

if __name__ == "__main__":
    twofa.twofactor_code()
