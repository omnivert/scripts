import sys
from time import sleep

if len(sys.argv) <= 3:
    print('usage: intervals.py reps rep_len break_len')
    print('       len is measured in seconds')
else:
    reps, rep_len, break_len = [*sys.argv[1:],]
    print('starting timer in...')
    for i in range(int(break_len), 0, -1):
        print('{}...'.format(i))
        sleep(1)
    for rep in range(int(reps), 0, -1):
        print('')
        print('#### start working! ####')
        print('{} reps remaining...'.format(rep-1))
        for d in range(int(rep_len), 0, -1):
            if d <= 5:
                print('{}...'.format(d))
            sleep(1)
        print('')
        print('#### break! ####')
        for d in range(int(break_len), 0, -1):
            if d <= 5:
                print('{}...'.format(d))
            sleep(1)
    print('')
    print('################')
    print('#### FINISH ####')
    print('################')

