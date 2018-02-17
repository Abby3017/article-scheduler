#!/bin/bash

export WORKON_HOME=~/.virtualenvs
VIRTUALENVWRAPPER_PYTHON='/usr/bin/python'
source ~/.local/bin/virtualenvwrapper.sh
PRGRM_DIR=~/program/py/crn_schedulre/
cd $PRGRM_DIR
workon reg_cod
python parser.py