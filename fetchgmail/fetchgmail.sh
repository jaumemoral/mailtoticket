#!/bin/sh
while true; do 
    python /mailtoticket/fetchgmail/fetchgmail.py
    if [ "x$HEARTBEAT_URL" != "x" ]; then
        python /mailtoticket/fetchgmail/heartbeat.py $HEARTBEAT_URL
    fi
    sleep 60
done