## Send mail if new articles on onkollywood.com
This program checks onkollywood.com for latest news and if there is any new it will mail people
who are mentioned in contacts.txt 

**mail can come in spam folder too**

Please provide your email id and password in parser.py file to get notification

Steps to run this program -
- `pip install -r requirements.txt` ( you can do that in virtualenv or in whole system )
- if you want to **run in one go** `python parser.py` will give desired output

If you want to run a cronjob -
- first run `crontab -e` 
- set this configuration ` m h  dom mon dow   command` (format in which to be written)

    `*/30 * * * * /crn_schedulre/run_parser.sh >> log.txt  2>&1`
    
    (file path where you keep run_parser.sh file) (and file path of log file and saving error)
    If you want to run by script

-  `. ./crn/schedulre/run_parser.sh` to run through command line as it has to run as source
otherwise `cd` command won't work

important part is **setting up virtualenv parameter** if you are using them
otherwise workon command and package installed will not show up
show check those file path and setting on your system
