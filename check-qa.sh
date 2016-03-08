#!/bin/sh
#
# Check QA
#

# compile all python files
python -m compileall -f -x '/(local|.git)/' -q .

# pass unit tests
python -m unittest discover

# comply with PEP8
PEP8=$(which pep8)

if [ -x "$PEP8" ]
then
	echo "INFO: Running PEP8 checks"
	pep8 --exclude '.git,local,settings_*' .
	pep8 settings_sample.py
else
	echo "WARNING! pep8 command not found, skipping PEP8 checks."
fi
