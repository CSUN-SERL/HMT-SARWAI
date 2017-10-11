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
import urllib
import numpy as np
import cv2

from emotiondetection.askmicrosoft import ask_microsoft

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

        # change to video stream ip
        stream = urllib.urlopen('http://192.168.1.45:8081/video.mjpg')

        bytes_data = ''

        frame = []
        while True:
            bytes_data += stream.read(1024)
            xd8 = bytes_data.find('\xff\xd8')
            xd9 = bytes_data.find('\xff\xd9')
            if xd8 != -1 and xd9 != -1:
                jpg = bytes_data[xd8:xd9+2]
                bytes_data = bytes_data[xd9+2:]
                frame = cv2.imdecode(
                    np.fromstring(jpg, dtype=np.uint8),
                    cv2.IMREAD_COLOR
                )
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                break

        emotions = ask_microsoft(frame, 'API KEY')
        if emotions is not None:
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
