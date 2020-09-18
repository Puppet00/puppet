from bs4 import BeautifulSoup
import requests
import os
import time
import random
import string
from lxml import html

print("Otomatik Kurulum Yapılıyor Hiçbir Tuşa Basmayınız . . .")
time.sleep(5)
os.system("pkg update && pkg install python libxml2 libxslt && pip install beautifulsoup4 && pip install html5lib && pip install --upgrade pip && pip install requests && pip install lxml")
os.system("clear")
print(" ")
phone_number = input("[+] Numaranızı Basında 0 Olmadan Giriniz : ")
print(" ")

while True:
    def id_generator(size=4, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))
    text = ("AG2X" + id_generator())
    headers = { 'User-Agent' : 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B137 Safari/601.1'}
    headers = { 'User-Agent' : 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14'}
    headers = { 'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0'}
    headers = { 'User-Agent' : 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3'}
    headers = { 'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)'}
    headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7'}
    headers = { 'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)'}
    headers = { 'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1'}
	
    login_data = {'__VIEWSTATE':'',
                  '__VIEWSTATEGENERATOR':'',
                  '__EVENTVALIDATION':'',
                  'phone': phone_number,
                  'promocode': text,
                  'btnSend': 'GÖNDER'
                  }
    with requests.Session() as s:
        url = 'https://appgalleryilehepkazan.com'
        r = s.get(url)
        soup = BeautifulSoup(r.content, 'html5lib')
        login_data['__VIEWSTATE'] = soup.find('input', attrs = {'name': '__VIEWSTATE'})['value']
        login_data['__VIEWSTATEGENERATOR'] = soup.find('input', attrs = {'name': '__VIEWSTATEGENERATOR'})['value']
        login_data['__EVENTVALIDATION'] = soup.find('input', attrs = {'name': '__EVENTVALIDATION'})['value']
        r = s.post(url, data=login_data, headers = headers)
        r.encoding = 'ISO-8859-1'
        extractedHtml = html.fromstring(r.content)
        message = extractedHtml.xpath("//*[@id='form1']/script[2]")
        print(message[0].text)
        print("_________________________________________________________________")
        #print(r.content)
