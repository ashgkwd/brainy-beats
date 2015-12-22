"""
Author: Ashish Gaikwad <ash.gkwd@gmail.com>
Copyright (c) 2015 Ashish Gaikwad

Description: This script will post a message on your slack channel
Please configure your `/etc/brainy-beats.cfg` file first.

Example brainy-beats.cfg

[slack]
url=https://hooks.slack.com/services/XxXxXxXxXx
channel=botwa
icon_emoji=ghost
username=beats-bot
"""

from subprocess import call
import sys
import json
import ConfigParser

def payload(text, conf):
	toPost = {
		"channel": "#" + conf.get("slack", "channel"),
		"username": conf.get("slack", "username"),
		"text": text,
		"icon_emoji": ":" + conf.get("slack", "icon_emoji") + ":"
	}
	return "payload=" + json.dumps(toPost)

def main():
	CONFIG_FILE = '/home/ash/Codes/brainy-beats.cfg'
	# read configuration 
	conf = ConfigParser.ConfigParser()
	conf.read(CONFIG_FILE)
	text = "Hello From Brainy Beats"

	if sys.argv[1] == "-f" and len(sys.argv) > 2:
		"""Read this file"""
		text = open(sys.argv[2]).read()
	else:
		text = sys.argv[1]

	call([
		"curl",
		"-X",
		"POST",
		"--data-urlencode",
		payload(text, conf),
		conf.get("slack", "url")
		])

if __name__ == '__main__':
	main()