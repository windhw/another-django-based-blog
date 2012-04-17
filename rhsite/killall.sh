#!/bin/bash
#Author  : HaoWei
#Date    : 2011.7.18
#Purpose : Monitor Mytunet and Restart it when necessary.
#This script runs every 2 hours. You can edit this scheme using "crontab -e"  
pids=$(ps aux | grep manage.py | grep -v grep | awk '{print $2}')
for pid in ${pids};do
	kill  ${pid}
done
