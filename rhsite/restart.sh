#!/bin/bash

# Replace these three settings.
PROJDIR="/home/haowei/rhcloud/a/wsgi/rhsite/"
PIDFILE="$PROJDIR/mysite.pid"
SOCKET="$PROJDIR/mysite.sock"

pids=$(ps aux | grep python | grep manage.py | grep -v grep | awk '{print $2}')
for pid in ${pids};do
	kill  ${pid}
done

cd $PROJDIR
if [ -f $PIDFILE ]; then
	rm -f -- $PIDFILE
fi
python manage.py runfcgi umask=0002 socket=$SOCKET pidfile=$PIDFILE
