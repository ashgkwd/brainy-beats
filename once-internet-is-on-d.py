"""
Author: Ashish Gaikwad <ash.gkwd@gmail.com>
Copyright (c) 2015 Ashish Gaikwad

Description: This daemon will execute command once
Internet is connected. Then it will exit.
"""
import socket
from subprocess import call
import time

commands = [["bash", "/usr/bin/beat.sh"]]

def internet(host='8.8.8.8', port=53):
	try:
		socket.setdefaulttimeout(1)
		socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
		return True
	except Exception as ex:
		pass
	return False

def main():
	print "[once-internet-is-on-d started]"
	while not internet():
		pass
	time.sleep(40)
	for x in commands:
		print "[once-internet-is-on-d calling] : ", x
		call(x)
	print "[once-internet-is-on-d finished]"

if __name__ == '__main__':
	main()