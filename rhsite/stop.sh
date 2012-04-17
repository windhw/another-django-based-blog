#!/bin/bash

# Replace these three settings.
PROJDIR="/home/haowei/rhcloud/a/wsgi/rhsite/"
PIDFILE="$PROJDIR/mysite.pid"
SOCKET="$PROJDIR/mysite.sock"

cd $PROJDIR
if [ -f $PIDFILE ]; then
	kill `cat -- $PIDFILE`
fi
