import pyotp
import os
import time
import subprocess

print(" ")
os.system("pip install pyotp")
os.system("pip3 install pyotp")
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
