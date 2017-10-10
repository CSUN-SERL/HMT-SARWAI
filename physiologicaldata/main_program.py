#!/usr/bin/env python

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import signal
import sys
import thread
import time
import urllib
import numpy as np
import cv2
#import os
from PyQt5 import QtWidgets, QtGui
#from PyQt5.QtWidgets import QFileDialog

import main_window
from utils.data_gatherer import DataGatherer  

def signal_handler(sig, frame):
    print('Do no use ctrl-c!')

signal.signal(signal.SIGINT, signal_handler)

class MainProgram(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
    _log_status = False

    def __init__(self, parent=None):
        super(MainProgram, self).__init__(parent)
        self.setupUi(self)
        self.__init_events()

        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(False)
        self.save_button.setEnabled(False)
        self.reset_all_button.setEnabled(False)
        self.reset_user_button.setEnabled(False)

        self.emotion_label.setStyleSheet('color: red')
        self.heart_label.setStyleSheet('color: red')
        self.gaze_label.setStyleSheet('color: red')
        self.gsr_label.setStyleSheet('color: red')

        self.video_stream_output.setScaledContents(True)

        self.__data = DataGatherer(1000, 0.1)

        try:
            thread.start_new_thread(self.__thread_realtime, ('Thread-1', 0.5))
            thread.start_new_thread(self.__thread_video_stream, ('Thread-2',))
        except Exception as err:
            print(err)

    def __init_events(self):
        self.start_button.clicked.connect(self.__start_button)
        self.stop_button.clicked.connect(self.__stop_button)
        self.save_button.clicked.connect(self.__save_button)
        self.reset_all_button.clicked.connect(self.__reset_all_button)
        self.reset_user_button.clicked.connect(self.__reset_user_button)
        self.set_user_button.clicked.connect(self.__set_user_button)
        #self.set_path_button.clicked.connect(self.__set_path_button)

    def __thread_video_stream(self, thread_name):
        # change to video stream ip
        stream = urllib.urlopen('http://96.10.1.168/mjpg/1/video.mjpg')
        bytes_data = ''

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

                height, width = frame.shape[:2]
                img = QtGui.QImage(
                    frame,
                    width,
                    height,
                    QtGui.QImage.Format_RGB888
                )
                img = QtGui.QPixmap.fromImage(img)
                self.video_stream_output.setPixmap(img)

    def __thread_realtime(self, thread_name, rate):
        """Thread method to capture data from device interface.
        """

        while True:
            time.sleep(rate) # controls the data logging rate
            #print(thread_name)
            self.__data.get_data(self._data_callback)

    def _data_callback(self, data, status):
        """_data is a callback method for the data gatherer.
        """

        self.emotion_output_label.setText('Emotion: {}'.format(data[0]))
        self.heart_output_label.setText('Heart: {}'.format(data[1]))
        self.delta_heart_output_label.setText('Delta Heart: {}'.format(data[2]))
        self.gaze_output_label.setText('Gaze: ({}, {})'.format(data[3], data[4]))
        self.gsr_output_label.setText('GSR: {}'.format(data[5]))

        if status[0] is True:
            self.emotion_label.setStyleSheet('color: green')
        else:
            self.emotion_label.setStyleSheet('color: red')

        if status[1] is True:
            self.heart_label.setStyleSheet('color: green')
        else:
            self.heart_label.setStyleSheet('color: red')

        if status[2] is True:
            self.gaze_label.setStyleSheet('color: green')
        else:
            self.gaze_label.setStyleSheet('color: red')

        if status[3] is True:
            self.gsr_label.setStyleSheet('color: green')
        else:
            self.gsr_label.setStyleSheet('color: red')


    def __start_button(self):
        if not self._log_status:
            self._log_status = True
            self.start_button.setEnabled(False)
            self.stop_button.setEnabled(True)
            self.save_button.setEnabled(False)
            self.reset_all_button.setEnabled(False)
            self.reset_user_button.setEnabled(False)
            self.__data.start_log()

    def __stop_button(self):
        if self._log_status:
            self._log_status = False
            self.start_button.setEnabled(True)
            self.stop_button.setEnabled(False)
            self.save_button.setEnabled(True)
            self.reset_all_button.setEnabled(True)
            self.reset_user_button.setEnabled(True)
            self.__data.stop_log()

    def __save_button(self):
        if not self._log_status:
            self.__data.save_log()

    def __reset_all_button(self):
        self.__data.reset_all_users()

    def __reset_user_button(self):
        self.__data.reset_user()

    def __set_user_button(self):
        user = self.set_user_textbox.text()
        if user is '' or user is None or not user:
            print('Invalid user!')
            return

        self.start_button.setEnabled(True)
        self.save_button.setEnabled(True)
        self.reset_all_button.setEnabled(True)
        self.reset_user_button.setEnabled(True)

        self.current_user_label.setText('User: {}'.format(user))
        self.__data.set_user(user)

    '''
    def __set_path_button(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.DirectoryOnly)
        dialog.setOption(QFileDialog.ShowDirsOnly, True)
        dialog.setOption(QFileDialog.DontUseNativeDialog, True)

        directory = dialog.getExistingDirectory(
            self,
            "Select Output Folder",
            os.path.expanduser('~'),
        )

        if directory:
            self.__data.set_path(directory)
            self.start_button.setEnabled(True)
            self.save_button.setEnabled(True)
            self.reset_all_button.setEnabled(True)
            self.reset_user_button.setEnabled(True)
    '''

def main():
    app = QtWidgets.QApplication(sys.argv)
    form = MainProgram()
    form.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
