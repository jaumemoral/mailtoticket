#!/bin/sh
python /mailtoticket/mailtoticket.py >/dev/null
# Volem que sempre acabi amb exit 0 perque aixi el fetchmail
# marqui el mail com a processat
exit 0