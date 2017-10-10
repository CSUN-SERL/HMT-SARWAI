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
#VIDEO_PORT = 5006
DATA_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

'''
cap = cv2.VideoCapture(0)

def thread_video_stream(thread_name):
    count = 0

    while count < 1:
        time.sleep(1)

        _, frame = cap.read() # (540, 960)

        img = cv2.resize(frame, (480, 640), interpolation=cv2.INTER_AREA)
        #img = img.flatten()
        bytes_str = img.tobytes()

        index = int(len(bytes_str)/20)
        for i in range(20):
            sock.sendto(bytes_str[i*index:(i+1)*index], (IP, VIDEO_PORT))

        count += 1

def signal_handler(sig, frame):
    cap.release()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
'''

def main():
    """Runs as main if python file is not imported
    """

    device_interface = ServerDeviceInterface()

    '''
    # Start thread on thread_data method with name Thread-1
    try:
        thread.start_new_thread(
            thread_video_stream,
            ('Thread-1', )
        )
    except Exception as e:
        print(e)
    '''

    while True:
        time.sleep(0.1)

        '''
        img = np.fromstring(bytes_str, dtype=np.uint8).reshape(540, 960)
        cv2.imshow('frame', img)
        '''

        data = {
            'data': device_interface.get_data(),
            'status': device_interface.get_status()
        }
        json_str = json.dumps(data)
        sock.sendto(json_str.encode(), (IP, DATA_PORT))

    #cap.release()

if __name__ == '__main__':
    main()
