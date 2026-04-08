#!/bin/sh
while true; do 
    python /mailtoticket/fetchgmail/fetchgmail.py 2>&1 > /tmp/mailtoticket.log
    STATUS=$?
    if [ "x$HEARTBEAT_URL" != "x" ]; then
        if [ "x$STATUS" == "x0" ]; then
            python /mailtoticket/fetchgmail/heartbeat.py $HEARTBEAT_URL
        fi
    fi
    if [ "x$HEARTBEAT_URL_ERROR" != "x" ]; then
        if [ "x$STATUS" != "x0" ]; then
            python /mailtoticket/fetchgmail/heartbeat.py $HEARTBEAT_URL_ERROR
        fi
    fi
    sleep 60
done