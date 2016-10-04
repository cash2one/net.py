#!/usr/bin/env python
# -*- coding: UTF-8 -*-


# finding out if your Python supports IPv6 sockets

import socket
import argparse
import netifaces as ni


def inspect_ipv6_support():
	print "IPv6 support built into Python: %s" % socket.has_ipv6
	ipv6_addr = {}
	for interface in ni.interfaces():
		all_addresses = ni.ifaddresses(interface)
		print "interface %s" % interface

		for family, addrs in all_addresses.iteritems():
			fam_name = ni.address_families[family]
			print "address family: %s" % fam_name
			for addr in addrs:
				if fam_name == 'AF_INET6':
					ipv6_addr[interface] = addr['addr']
				print "Address: %s" % addr['addr']
				nmask = addr.get('netmask', None)
				if nmask:
					print "netmask: %s" % nmask
				bcast = addr.get('broadcast', None)
				if bcast:
					print 'broadcast: %s' % bcast
	
	if ipv6_addr:
		print "Found IPv6 address: %s" % ipv6_addr
	else:
		print "No IPv6 address found"


if __name__ == "__main__":
	inspect_ipv6_support()
