#! /usr/bin/env python

# setting and getting the default socket timeout


import socket


def test_socket_timeout():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print ("Default socket timeout: %s" % s.gettimeout())
	s.settimeout(100)
	print ("current socket timeout: %s" % s.gettimeout())


if __name__ == '__main__':
	test_socket_timeout()
