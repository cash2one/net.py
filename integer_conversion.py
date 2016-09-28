#! /usr/bin/env python

# convering integers to and from host to network byte order


import socket


def convert_integer():
	data = 1234
	# 32-bit
	print ("original: %s => Long host byte order: %s, network byte order: %s" % 
		(data, socket.ntohl(data), socket.htonl(data)))
	# 16-bit
	print ("original: %s => Short host byte order: %s, networ byte order: %s" %
		(data, socket.ntohs(data), socket.htons(data)))


if __name__ == '__main__':
	convert_integer()
