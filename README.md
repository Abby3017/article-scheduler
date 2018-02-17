

How to run cron job for this task -
first run crontab -e 
set this configuration
# m h  dom mon dow   command
/home/abby/program/py/crn_schedulre/run_parser.sh >> /home/abby/program/py/output.txt  2>&1

(file path where you keep run_parser.sh file)

Setting up run_parser bash file - 
. ./ to run through command line as it has to run as source
otherwise cd command won't work
important part is setting up virtualenv parameter otherwise workon command and package installed will not show up
show check those file path and setting on your system

print('hello world')

jbkndcwmuyeqhfrj