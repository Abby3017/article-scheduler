#!/bin/bash

echo "hello,world"
export WORKON_HOME=~/.virtualenvs
VIRTUALENVWRAPPER_PYTHON='/usr/bin/python'
source /home/abby/.local/bin/virtualenvwrapper.sh
PRGRM_DIR=/home/abby/program/py/crn_schedulre/
cd $PRGRM_DIR
workon reg_cod
python parser.py