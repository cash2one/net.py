#! /usr/bin/env python

# retrieving a remote machine's IP Address

import socket


def get_remote_machine():
	remote_host = "www.baidu.com"
	
	try:
		print ("IP Address of baidu.com: %s" % socket.gethostbyname(remote_host))

	except socket.error, err_msg:
		print ("%s: %s" % (remote_host, err_msg))
	
if __name__ == '__main__':
	get_remote_machine()
