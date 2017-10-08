#!/usr/bin/env python

"""Retrieve data from external devices and software.

This module retrieves data from devices and software (e.g. Emotion Detection,
Heart Rate, Gaze Tracking, and Galvanic Skin Response), and sends the data
using network sockets.
"""

from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
import random
import operator
import math
import time
import socket
import json

class ServerDeviceInterface(object):
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

        self._previous_heart_rate = None
        self._previous_time = None

    def __round_float(self, val):
        """Rounds floating point to the second decimal place.
        """

        return math.ceil(val*100)/100

    def get_status(self):
        """Gets status from the devices.

        Status is retrieved from external devices and software and saves it in an
        array.

        Returns:
            Dictionary: Contains device status.
        """

        status_set = [
            self._emotion_status,
            self._heart_rate_status,
            self._gaze_status,
            self._gsr_status
        ]

        return status_set

    def get_data(self):
        """Gets data from the devices.

        Data is retrieved from external devices and software and saves it in an
        array.

        Returns:
            Dictionary: Contains devices data.
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
            rate = int(random.uniform(60, 70))
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

        if self._previous_heart_rate is None and isinstance(data_set[1], int):
            self._previous_heart_rate = data_set[1]
            self._previous_time = time.time()

        return data_set

def main():
    """Runs as main if python file is not imported
    """
    IP = '127.0.0.1'
    PORT = 5005

    device_interface = ServerDeviceInterface()

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        time.sleep(0.1)

        data = {
            'data': device_interface.get_data(),
            'status': device_interface.get_status()
        }
        json_str = json.dumps(data)
        sock.sendto(json_str.encode(), (IP, PORT))


if __name__ == '__main__':
    main()
