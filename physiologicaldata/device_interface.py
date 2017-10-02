from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
import random
import operator
import math

class DeviceInterface(object):
    _NA = 'N/A'

    def __init__(self):
        self._emotion_data = True
        self._heart_data = True
        self._gaze_data = True

    def __round_float(self, val):
        """Rounds floating point to the second decimal place.
        """

        return math.ceil(val*100)/100

    def get_data(self, data):
        data_set = []

        if self._emotion_data:
            emotions = {
                'angry': random.uniform(0, 1),
                'disgust': random.uniform(0, 1),
                'fear': random.uniform(0, 1),
                'happy': random.uniform(0, 1),
                'sad': random.uniform(0, 1),
                'surprise': random.uniform(0, 1),
                'neutral': random.uniform(0, 1)
            }
            data_set += [max(emotions.iteritems(), key=operator.itemgetter(1))[0]]
        else:
            data_set += [self._NA]

        if self._heart_data:
            data_set += [int(random.uniform(60, 120))]
        else:
            data_set += [self._NA]

        if self._gaze_data:
            data_set += [
                int(random.uniform(0, 1920)),
                int(random.uniform(0, 1080))
            ]
        else:
            data_set += [self._NA, self._NA]

        data(data_set)

def main():
    """Runs as main if python file is not imported
    """

    pass

if __name__ == '__main__':
    main()
