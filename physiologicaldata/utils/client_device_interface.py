"""Retrieve data from server device interface.

This module retrieves data from server device interface and sends the data
as a parameter through a callback function.
"""

from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
import socket
import json

class ClientDeviceInterface(object):
    """Device Interface manages data from devices and software.

    Data is retrieved from server device interface, and calls an external
    callback function with the devices data.
    """

    _IP = '127.0.0.1'
    _PORT = 5005

    def __init__(self):
        """Initializes DeviceInterface.

        Device availability is determined.
        """
        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__sock.bind((self._IP, self._PORT))

    def get_data(self, data_callback):
        """Gets data from the devices.

        Data is retrieved from external devices and software and saves it in an
        array. This array is passed as an argument to the 'data' callback
        function.

        Args:
            data_callback (function): Callback function with array parameter.
        """

        json_data, _ = self.__sock.recvfrom(1024)
        data_dict = json.loads(json_data.decode())

        #status_set = ['N/A', 'N/A', 'N/A', 'N/A']
        #data_set = ['N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A']
        #data_dict = {'data': data_set, 'status': status_set}

        data_callback(data_dict) # call callback function with data set

def main():
    """Runs as main if python file is not imported
    """

    pass

if __name__ == '__main__':
    main()
