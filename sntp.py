#! /usr/bin/env python

# writing a simple SNTP client
# there is some errors !!!

import sys
import socket
import time
import struct

NTP_SERVER = "0.uk.pool.ntp.org"
TIME1970 = 2208988800L

def sntp_client():
	client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	data = '\xlb' + 47 * '\0'
	client.sendto(data, (NTP_SERVER, 123))
	data, address = client.recvfrom(1024)
	if data:
		print ('Response reveiced from: ', address)
	
	t = struct.unpack('!12I', data)[10]
	t -= TIME1970
	print ("\tTIME1970" % time.ctime(t))



if __name__ == '__main__':
	sntp_client()



