#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import os
import socket
import threading
import SocketServer

SERVER_HOST = "localhost"
SERVER_PORT = 0 # Lells the kernel to pick up a port dynamically
BUF_SIZE = 1024

def client(ip, port, message):
	""" A client to test threading mixin server """
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((ip, port))
	try:
		sock.sendall(message)
		response = sock.recv(BUF_SIZE)
		print "Client reveiced: %s" % response
	finally:
		sock.close()

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):
	""" An example of threaded TCP request handler """
	def handle(self):
		data = self.request.recv(BUF_SIZE)
		current_thread = threading.current_thread()
		response = "%s: %s" % (current_thread.name, data)
		self.request.sendall(response)


class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
	"""Nothing to add here, inherited  everything necessary from parents """
	pass


if __name__ == "__main__":
	# Run server
	server = ThreadedTCPServer((SERVER_HOST, SERVER_PORT), ThreadedTCPRequestHandler)
	ip, port = server.server_address; # reveice ip address
	# start a therad with the server -- one thread per request
	server_thread = threading.Thread(target=server.serve_forever)
	# Exit the server thread when the main thread exits
	server_thread.setDaemon = True
	server_thread.start()
	print "Server loop running on thread: %s" % server_thread.name
	# Run clients
	client(ip, port, "hello from client1")
	client(ip, port, "hello from client2")
	client(ip, port, "hello from client3")
	# server cleanup
	server.shutdown()







































