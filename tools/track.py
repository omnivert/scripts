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
from datetime import datetime, timedelta
parser = argparse.ArgumentParser()
#this one's trickier than i thought
#parser.add_argument('-l', '--list', help='display last 5 lines of todays file', action='store_true')
parser.add_argument('-m', '--message', help='append message according to flag, default to current')
parser.add_argument('-c', '--message_current', help='append newline, date, message', action='store_true')
parser.add_argument('-a', '--message_additional', help='append newline, message', action='store_true')
parser.add_argument('-p', '--message_previous', help='append message, newline, date', action='store_true')
parser.add_argument('-d', '--log_dir', help='set and save log_dir')
parser.add_argument('-b', '--breakpoint', help='set and save file breakpoint (HHMM)')
args = parser.parse_args()

# mkdir -p ~/.config/track
confdir = Path(Path.home(), '.config', 'track') 
confdir.mkdir(parents=True, exist_ok=True)

trackrc = Path(confdir, 'trackrc')
trackrc.touch(exist_ok=True)

brkpoint = '0400'
logdir = Path.cwd()

if args.log_dir:
    logdir = Path(args.log_dir)
    if not logdir.is_dir():
        print('please specify a valid log directory')
        exit(1)

if args.breakpoint:
    brkpoint = args.breakpoint
    # add some try-catch to check if it's formatted properly

# pull info from trackrc, update if necessary
# TODO deal with first run case, no args, no trackrc
with open(str(trackrc), 'r+') as f:
    content = f.read()
    if len(content) > 0:
        logdir_stored, brkpoint_stored = [x.split(':')[1] for x in content.split('\n')[:2]]
        if not args.log_dir:
            logdir = logdir_stored
        brkpoint = brkpoint_stored

    # write every time cause it's nicer code to read
    f.seek(0)
    f.write('logdir:{}\nbreakpoint:{}'.format(logdir, brkpoint))

now = datetime.now()

filenameformat = 'task_tracker_{}'#.format(timestamp[:10])
# need to stop and think about this one
if now.time() < datetime.strptime(brkpoint, '%H%M').time():
    filedate = now - timedelta(hours=24)
else:
    filedate = now
filename = filenameformat.format(filedate.strftime('%Y-%m-%d'))
    
logfile = Path(logdir, filename)
logfile.touch(exist_ok=True)

timestamp = now.strftime('%Y-%m-%d_%H%M')

###### now we actually write things ######

if args.message:
    with open(str(logfile), 'a') as f:
        message_string = ''
        if args.message_current:
            message_string = '{} {}\n'.format(timestamp, args.message)
        elif args.message_additional:
            message_string = '{}\n'.format(args.message)
        elif args.message_previous:
            message_string = '{}\n{} '.format(args.message, timestamp)
        else:
            message_string = '{} {}\n'.format(timestamp, args.message)
        f.write(message_string)

print(timestamp)


