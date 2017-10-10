#!/usr/bin/env python

from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
import time
import signal
import sys
import socket
import json
import thread
import cv2

from utils.server_device_interface import ServerDeviceInterface

IP = '127.0.0.1'
PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

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
        sock.sendto(json_str.encode(), (IP, PORT))

if __name__ == '__main__':
    main()
