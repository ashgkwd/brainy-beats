#!/bin/bash
# Author: Ashish Gaikwad <ash.gkwd@gmail.com>
# Copyright (c) 2015 Ashish Gaikwad

# Description: This script will generate health report of the system.
# It's designed for BeagleBone health testing; but I hope it can be used
# in other OS without any major changes.

OUTPUT_LOG="/tmp/beat.log";

# Let's run basic system status commands
echo "[who]" > $OUTPUT_LOG; 
who -b >> $OUTPUT_LOG;
who -q >> $OUTPUT_LOG;

echo "[ifconfig]" >> $OUTPUT_LOG;
ifconfig | grep inet >> $OUTPUT_LOG;

echo "[ls /dev/tty*]" >> $OUTPUT_LOG;
ls /dev/tty* | xargs -n10 >> $OUTPUT_LOG;

# call post-to-slack.py to send health report
python /usr/bin/post-to-slack.py -f $OUTPUT_LOG;
