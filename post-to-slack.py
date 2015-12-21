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
	CONFIG_FILE = '/etc/slack_post.cfg'
	# read configuration 
	conf = ConfigParser.ConfigParser()
	conf.read(CONFIG_FILE)

	call([
		"curl",
		"-X",
		"POST",
		"--data-urlencode",
		payload(sys.argv[1], conf),
		conf.get("slack", "url")
		])

if __name__ == '__main__':
	main()