#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# extracting cookie infomation after visiting a website

import cookielib
import urllib
import urllib2

ID_USERNAME = 'id_username'
ID_PASSWORD = 'id_password'
USERNAME = 'withtz@163.com'
PASSWORD = '123456'
LOGIN_URL = 'https://bitbucket.org/account/signin/?next=/'
NORMAL_URL = 'https://bitbucket.org/'


def extract_cookie_info():
	"""fake login to a site which cookie"""
	# setup cookie jar
	cj = cookielib.CookieJar()
	login_data = urllib.urlencode({ID_USERNAME: USERNAME, 
		ID_PASSWORD: PASSWORD})
	# create url opener
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
	resp = opener.open(LOGIN_URL, login_data)

	# Send login info
	for cookie in cj:
		print "----first time cookie: %s --> %s" % (cookie.name, cookie.value)
	print "Headers: %s" % resp.headers


if __name__ == '__main__':
	extract_cookie_info()


	
	
