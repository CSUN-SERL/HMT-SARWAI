#!/usr/bin/env python

from __future__ import print_function, division, absolute_import
import os

from logger import DataLogger
from device_interface import DeviceInterface

class DataGatherer(object):
    _COLUMNS = ['emotion', 'bpm', 'gaze-x', 'gaze-y']

    def __init__(self, limit, name):
        self._limit = limit
        self.__data_log = DataLogger(
            self._limit,
            columns=self._COLUMNS,
            path='/home/danny/Desktop/users/{}'.format(name)
        )
        self.__device_interface = DeviceInterface()

    def _data(self, data):
        self.__data_log.log(data)

    def check(self):
        self.__device_interface.get_data(self._data)

    def save(self):
        self.__data_log.save()

    def reset_all(self):
        pass

    def reset_session(self):
        pass
    
    def reset_user(self):
        pass
    
    def get_user(self):
        pass

    def set_user(self):
        pass

def main():
    """Runs as main if python file is not imported
    """

    pass

if __name__ == '__main__':
    main()
