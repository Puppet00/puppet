import urllib.request
import random
from bs4 import BeautifulSoup
import sys

def user_agent():
    
    useragent = [
        "Mozilla/5.0 CK={ } (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
        "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:24.0) Gecko/20100101 Firefox/24.0",
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a1) Gecko/20070308 Minefield/3.0a1",
        "Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko; googleweblight) Chrome/38.0.1025.166 Mobile Safari/535.19",
        "Mozilla/5.0 (Linux; Android 6.0.1; RedMi Note 5 Build/RB3N5C; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/68.0.3440.91 Mobile Safari/537.36",
    ]

    return random.choice(useragent)

def parseIP(htmlIP):
    output = str(htmlIP)[4:]
    output = output[:len(output)-5]

    return str(output).strip()


def file_writer(data):
    opnr = open("parsedIP.txt", "a+")
    for x in data:
        opnr.write(x+"\n")
    
    opnr.close()
    

def parsetd(url="https://us-proxy.org/"):
    url ="https://free-proxy-list.net/"
    url ="https://free-proxy-list.net/uk-proxy.html"
    url ="https://www.sslproxies.org/"
    url ="https://free-proxy-list.net/anonymous-proxy.html"
    url ="https://www.socks-proxy.net/"
    req = urllib.request.Request(url, headers={"User-Agent": user_agent()})
    data = urllib.request.urlopen(req).read().decode()
    soup = BeautifulSoup(data, features="html.parser")
    tag = soup.findAll('td')
    output = []
    st = ""
    
    for x in tag:
        if parseIP(x)[0].isdigit() and "." in parseIP(x) and st == "":
            st += parseIP(x)
        elif parseIP(x)[0].isdigit() and not "." in parseIP(x) and st != "":
            st += ":"+parseIP(x)
            output.append(st.strip())
            print(st)
            st = ""
        else:
            continue
    
    return output

try:
    file_writer(parsetd(sys.argv[1]))
except IndexError:
    print("Using Default website to parse proxy List td\nYou can use another site to parse type python proxyParsedtd.py [Site]\nparsed proxies will be saved in parsedIP.txt")
    file_writer(parsetd())


print("[+]Saved in parsedIP.txt")
