#!/usr/bin/env python

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import json
import socket
import time

from utils.server_device_interface import ServerDeviceInterface

IP = '127.0.0.1'  # change to target computer
PORT = 5005

SOCK = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#SOCK.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#SOCK.bind((IP, PORT))

def main():
    """Runs as main if python file is not imported
    """

    device_interface = ServerDeviceInterface()

    try:
        while True:
            time.sleep(0.1)

            data = {'data': device_interface.get_data()}
            json_str = json.dumps(data)
            print(json_str)

            SOCK.sendto(json_str.encode(), (IP, PORT))
    except KeyboardInterrupt:
        SOCK.close()

if __name__ == '__main__':
    main()
