#! /usr/bin/env python
# -*- coding: utf-8 -*-

# sending web requests through a proxy server


import urllib

URL = 'https://www.github.com'
PROXY_ADDRESS = '61.185.219.126:3128'

if __name__ == '__main__':
	resp = urllib.urlopen(URL, proxies = {'http': PROXY_ADDRESS})
	print "Proxy server returns response headers: %s" % resp.headers
