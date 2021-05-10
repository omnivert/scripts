#!/usr/bin/env python

# python >= 3.5

# PLAN
# format will be 'track [-m "what i'm about to do"] [-p "what i just did"] [-d log_dir] [-l]'
# no args will just add '\nTIMESTAMP'
# -p will add 'COMMENT\nTIMESTAMP'
# -m will add '\nTIMESTAMPCOMMENT'
# -l will tail -n 4 or something the file
# stores logs in log_dir
# log_dir defaults to current directory or what's in ~/.config/track/trackrc
# first run creates ~/.config/track/trackrc if it doesn't exist
#   populates with log_dir (default pwd), breakpoint (default 04:00)
# if -d:
#   writes log_dir to trackrc
# loads trackrc
# first run of the day creates logfile logdir/DATE_personal_log.txt
#   basically we just make the file if it's not there
# if -l:
#   print last n lines of logfile
# else:
#   opens logfile
#   writes TIMESTAMP COMMENT in the order specified by flags
# done

import argparse
from pathlib import Path
parser = argparse.ArgumentParser()
parser.add_argument('-l', '--list', help='display last 5 lines of todays file', action='store_true')
parser.add_argument('-m', '--message_current', help='append newline, date, message')
parser.add_argument('-a', '--message_additional', help='append newline, message')
parser.add_argument('-p', '--message_previous', help='append message, newline, date')
parser.add_argument('-d', '--log_dir', help='set and save log_dir', action='store_true')
parser.parse_args()

# mkdir -p ~/.config/track
confdir = Path(Path.home(), '.config', 'track') 
confdir.mkdir(parents=True, exist_ok=True)



print('hello')


