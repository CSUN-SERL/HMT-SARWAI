#!/usr/bin/env python

from __future__ import print_function, division, absolute_import
import random

class DeviceInterface(object):
    def __init__(self):
        pass

    def get_emotion(self, emotion):
        emotions = [
            random.uniform(0, 1),
            random.uniform(0, 1),
            random.uniform(0, 1),
            random.uniform(0, 1),
            random.uniform(0, 1),
            random.uniform(0, 1),
            random.uniform(0, 1)
        ]
        emotion(emotions)

    def get_eye_gaze(self, eye_gaze):
        gaze = [
            random.uniform(0, 255),
            random.uniform(0, 255)
        ]
        eye_gaze(gaze)

    def get_heart_rate(self, heart_rate):
        heart = [random.uniform(60, 120)]
        heart_rate(heart)

def main():
    """Runs as main if python file is not imported
    """

    pass

if __name__ == '__main__':
    main()
