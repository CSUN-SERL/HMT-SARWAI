"""Retrieve data from server device interface.

This module retrieves data from server device interface and sends the data
as a parameter through a callback function.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import json
import socket

class ClientDeviceInterface(object):
    """Device Interface manages data from devices and software.

    Data is retrieved from server device interface, and calls an external
    callback function with the devices data.
    """

    _IP = ''  # DO NOT CHANGE
    _PORT = 5005

    def __init__(self):
        """Initializes DeviceInterface.

        Device availability is determined.
        """

        self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._sock.bind((self._IP, self._PORT))
        self._sock.settimeout(2)

    def get_data(self, data_callback):
        """Gets data from the devices.

        Data is retrieved from external devices and software and saves it in an
        array. This array is passed as an argument to the 'data' callback
        function.

        Args:
            data_callback (function): Callback function with array parameter.
        """

        data_dict = {}
        try:
            json_data, _ = self._sock.recvfrom(1024)
            data_dict = json.loads(json_data.decode())
        except socket.timeout as err:
            print('Connection {}'.format(err))

            #status_set = [False, False, False, False]
            data_set = ['N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A']
            data_dict = {
                'data': data_set
                #'status': status_set
            }
        finally:
            data_callback(data_dict)  # call callback function with data set

def main():
    """Runs as main if python file is not imported
    """

    pass

if __name__ == '__main__':
    main()
