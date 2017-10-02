#!/usr/bin/env python

from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
import signal
import sys
import time

from data_gatherer import DataGatherer  

def signal_handler(sig, frame):
    print('Exiting program.')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def main():
    data = DataGatherer(1000, 0.1, 'danny')

    #data.reset_all()
    #data.reset_user('danny')

    data.start()

    count = 0
    while count < 10:
        time.sleep(1)
        count += 1

    data.stop()
    data.save()

if __name__ == '__main__':
    main()
