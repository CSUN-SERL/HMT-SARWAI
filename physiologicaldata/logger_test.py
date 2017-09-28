#!/usr/bin/env python

from __future__ import print_function, division, absolute_import
import time

from data_gatherer import DataGatherer

def main():
    data = DataGatherer(1000)
    count = 0

    while True:
        count += 1
        if count > 20:
            break

        data.check()
        time.sleep(0.1)

    data.save()

    print('All data logged.')

if __name__ == '__main__':
    main()
