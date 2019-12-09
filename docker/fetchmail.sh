#!/bin/sh
# Sembla que dona problemes al canviar els permisos del fitxer,
# aixi que treballarem amb una copia fora del /conf
# Si fem canvis al fitxer del volum haurem de rearrencar el docker
cp /conf/fetchmailrc /mailtoticket/fetchmailrc
chmod 700 /mailtoticket/fetchmailrc
while true; do fetchmail --silent -f /mailtoticket/fetchmailrc 2>/dev/null; sleep 60; done
