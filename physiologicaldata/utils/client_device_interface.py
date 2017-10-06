"""Retrieve data from external devices and software.

This module retrieves data from devices and software (e.g. Emotion Detection,
Heart Rate, Gaze Tracking, and Galvanic Skin Response), and sends the data
through a callback function.
"""

from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
import random
import operator
import math

class DeviceInterface(object):
    """Device Interface manages data from devices and software.

    Data is retrieved from external devices and software, and calls an external callback
    function with the devices data.
    """

    _NA = 'N/A' # specifies the output if a device is not available

    def __init__(self):
        """Initializes DeviceInterface.

        Device availability is determined.
        """
        self._emotion_status = True
        self._heart_rate_status = True
        self._gaze_status = True
        self._gsr_status = True

    def __round_float(self, val):
        """Rounds floating point to the second decimal place.
        """

        return math.ceil(val*100)/100

    def get_status(self, status_callback):
        """Gets status from the devices.

        Status is retrieved from external devices and software and saves it in an
        array. This array is passed as an argument to the 'status' callback
        function.

        Args:
            status_callback (function): Callback function with array parameter.
        """

        status_set = [
            self._emotion_status,
            self._heart_rate_status,
            self._gaze_status,
            self._gsr_status
        ]

        status_callback(status_set) # call callback function with status set

    def get_data(self, data_callback):
        """Gets data from the devices.

        Data is retrieved from external devices and software and saves it in an
        array. This array is passed as an argument to the 'data' callback
        function.

        Args:
            data_callback (function): Callback function with array parameter.
        """

        data_set = []

        if self._emotion_status:
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

        if self._heart_rate_status:
            data_set += [int(random.uniform(60, 120))]
        else:
            data_set += [self._NA]

        if self._gaze_status:
            data_set += [
                int(random.uniform(0, 1920)),
                int(random.uniform(0, 1080))
            ]
        else:
            data_set += [self._NA, self._NA]

        if self._gsr_status:
            data_set += [self.__round_float(random.uniform(0, 5))]
        else:
            data_set += [self._NA]

        data_callback(data_set) # call callback function with data set

def main():
    """Runs as main if python file is not imported
    """

    pass

if __name__ == '__main__':
    main()
