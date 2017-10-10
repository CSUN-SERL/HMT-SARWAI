#!/usr/bin/env python

from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
import time
import socket
import json

from utils.server_device_interface import ServerDeviceInterface

IP = '127.0.0.1'
PORT = 5005

SOCK = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def main():
    """Runs as main if python file is not imported
    """

    device_interface = ServerDeviceInterface()

    while True:
        time.sleep(0.1)

        data = {
            'data': device_interface.get_data(),
            'status': device_interface.get_status()
        }
        json_str = json.dumps(data)
        SOCK.sendto(json_str.encode(), (IP, PORT))

if __name__ == '__main__':
    main()
