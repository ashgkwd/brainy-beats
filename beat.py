"""
Author: Ashish Gaikwad <ash.gkwd@gmail.com>
Copyright (c) 2015 Ashish Gaikwad

Description: This script will generate health report of the system.
It's designed for BeagleBone health testing; but I hope it can be used
in other OS without any major changes.
"""

from subprocess import call
import ConfigParser

def run_and_save(command, output="/tmp/beat."):
	command_output = "/tmp/beat.log"
	to_run = [
	command + [">", command_output],
		["echo", "[output]", ">>", output],
		["echo", command[0], ">>", output],
		["cat", command_output, ">>", output]
	]
	for x in to_run:
		call(x)

def beat():
	"""Run commands and upload output"""

if __name__ == '__main__':
	beat()