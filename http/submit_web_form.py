#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import requests
import urllib
import urllib2


ID_USERNAME = 'signup-user-name'
ID_EMAIL = 'signup-user-email'
ID_PASSWORD = 'signup-user-password'
USERNAME = 'username'
EMAIL = 'you@email.com'
PASSWORD = 'yourpassword'
SIGNUP_URL = 'https://ssl.zc.qq.com/chs/index.html'


def submit_form():
	"""submit a form """
	payload = {ID_USERNAME: USERNAME,
				ID_EMAIL: EMAIL,
				ID_PASSWORD: PASSWORD,}
	
	# Make a get request
	resp = requests.post(SIGNUP_URL)
	print "Requests from a POST request: %s" % resp.content

	# send POST request
	resp = requests.post(SIGNUP_URL, payload)
	print "Headers from a POST request response: %s" % resp.headers
	#print "HTML Response: %s" % resp.read()


if __name__ == '__main__':
	submit_form()
