#! /usr/bin/env python

import socket
import sys
import argparse

host = "localhost"

def echo_client(port):
	"""A simple echo simple"""
	# create a  TCP/IP socket 
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#connect the socket to the server
	server_address = (host, port)
	print "connecting to %s port %s" % server_address
	sock.connect(server_address)

	# send data
	try:
		message = "test message. This will be echoed"
		print "sending %s" % message
		sock.sendall(message)
		# look for the response
		amount_received = 0
		amount_expected = len(message)
		while amount_received < amount_expected:
			data = sock.recv(16)
			amount_received += len(data)
			print "received: %s" % data
	except socket.error, e:
		print "socket error: %s " % str(e)
	finally:
		print "closing connection to the server\n"
		sock.close()
	


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="socket server example")
	parser.add_argument('--port', action="store", dest="port", type=int, required=True)
	given_args = parser.parse_args()
	port = given_args.port
	echo_client(port)

