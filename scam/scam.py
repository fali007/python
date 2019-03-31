import os
import requests
import json
import random
import string

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed=(os.urandom(1024))

url="https://accounts.craigslist.org/login?lang=en&cc=us"

names = json.loads(open('namelist.json').read())

for name in names:
	name_extra = ''.join(random.choice(string.digits))

	username = name.lower() + name_extra + '@gmail.com'
	password = ''.join(random.choice(chars) for i in range(8))
	requests.post(url, allow_redirects= False,data={
		'inputEmailHandle' : username,
		'inputPassword' : password
		})
	print("sending username %s and password %s"%(username,password))
# print(chars for i in range(10))

# https://accounts.craigslist.org/login?lang=en&cc=us

