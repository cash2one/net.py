#!/usr/bin/env python
# -*- coding: utf-8 -*-

# listing the files in a remote ftp server

import ftplib

FTP_SERVER_URL = 'ftp.kernel.org'

def test_ftp_connection(path, username, email):
	# open ftp connection
	ftp = ftplib.FTP(path, username, email)

	# list files in the /pub directory
	ftp.cwd('/pub')
	print "File list at %s: " % path
	files = ftp.dir()
	print files

	ftp.quit()


if __name__ == '__main__':
	test_ftp_connection(path=FTP_SERVER_URL,
		username='anonymous', email='nobody@nourl.com')

