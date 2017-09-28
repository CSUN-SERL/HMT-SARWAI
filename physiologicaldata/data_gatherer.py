#!/usr/bin/env python

from __future__ import print_function, division, absolute_import

from logger import DataLogger
from device_interface import DeviceInterface

class DataGatherer(object):
    _EMOTION_COLUMNS = [
        'angry',
        'disgust',
        'fear',
        'happy',
        'sad',
        'surprised',
        'neutral'
    ]
    _GAZE_COLUMNS = ['x', 'y']
    _HEART_COLUMNS = ['bpm']
    #_GSR_COLUMNS = ['i dont know']

    def __init__(self, limit):
        self._limit = limit
        self.__emotion_log = DataLogger(
            self._limit,
            columns=self._EMOTION_COLUMNS,
            name='emotion'
        )
        self.__gaze_log = DataLogger(
            self._limit,
            columns=self._GAZE_COLUMNS,
            name='gaze'
        )
        self.__heart_log = DataLogger(
            self._limit,
            columns=self._HEART_COLUMNS,
            name='heart'
        )
        self.__device_interface = DeviceInterface()

    def _emotion(self, data):
        self.__emotion_log.log(data)

    def _eye_gaze(self, data):
        self.__gaze_log.log(data)

    def _heart_rate(self, data):
        self.__heart_log.log(data)

    def check(self):
        self.__device_interface.get_emotion(self._emotion)
        self.__device_interface.get_eye_gaze(self._eye_gaze)
        self.__device_interface.get_heart_rate(self._heart_rate)

    def save(self):
        self.__emotion_log.save()
        self.__gaze_log.save()
        self.__heart_log.save()

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
