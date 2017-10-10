"""Retrieve data from external devices and software.

This module retrieves data from devices and software (e.g. Emotion Detection,
Heart Rate, Gaze Tracking, and Galvanic Skin Response), and sends the data
using network sockets.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import math
import operator
import random
import time

# FOR LINUX
from neulog_data import neulog_api
# FOR WINDOWS
#from physiologicaldata.neulog_data import neulog_api

class ServerDeviceInterface(object):
    """Device Interface manages data from devices and software.

    Data is retrieved from external devices and software, and calls an external callback
    function with the devices data.
    """

    _NA = 'N/A'  # specifies the output if a device is not available

    def __init__(self):
        """Initializes DeviceInterface.

        Device availability is determined.
        """

        self._previous_heart_rate = None
        self._previous_time = None

    def __round_float(self, val):
        """Rounds floating point to the second decimal place.
        """

        return math.ceil(val*100)/100

    def get_data(self):
        """Gets data from the devices.

        Data is retrieved from external devices and software and saves it in an
        array.

        Returns:
            Dictionary: Contains devices data.
        """

        data_set = []

        emotion = None
        if emotion is not None:
            emotions = {
                'angry': random.uniform(0, 1),
                'disgust': random.uniform(0, 1),
                'fear': random.uniform(0, 1),
                'happy': random.uniform(0, 1),
                'sad': random.uniform(0, 1),
                'surprise': random.uniform(0, 1),
                'neutral': random.uniform(0, 1)
            }
            # get emotion key based on highest value.
            data_set += [max(emotions.iteritems(), key=operator.itemgetter(1))[0]]
        else:
            data_set += [self._NA]

        rate = neulog_api.get_pulse_value()
        if isinstance(rate, int) or isinstance(rate, float):
            data_set += [rate]

            if self._previous_heart_rate is not None:
                delta_heart_rate = abs(rate - self._previous_heart_rate)
                #delta_time = time.time() - self._previous_time
                #delta_time /= 60
                self._previous_heart_rate = rate
                #self._previous_time = time.time()
                data_set += [delta_heart_rate]
            else:
                data_set += [self._NA]
        else:
            data_set += [self._NA, self._NA]

        gaze = None
        if gaze is not None:
            data_set += [
                int(random.uniform(0, 1920)),
                int(random.uniform(0, 1080))
            ]
        else:
            data_set += [self._NA, self._NA]

        gsr = neulog_api.get_gsr_value()
        if isinstance(gsr, float):
            data_set += [gsr]
        else:
            data_set += [self._NA]

        if self._previous_heart_rate is None and isinstance(data_set[1], int):
            self._previous_heart_rate = data_set[1]
            self._previous_time = time.time()

        return data_set

def main():
    """Runs as main if python file is not imported
    """

    pass

if __name__ == '__main__':
    main()
