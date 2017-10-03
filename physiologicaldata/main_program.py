from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
import sys
import signal
from PyQt5 import QtCore, QtGui, QtWidgets

import main_window
from data_gatherer import DataGatherer  

def signal_handler(sig, frame):
    print('Do no use ctrl-c!')

signal.signal(signal.SIGINT, signal_handler)

class MainProgram(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
    _logging = False

    def __init__(self, parent=None):
        super(MainProgram, self).__init__(parent)
        self.setupUi(self)
        self.__init_events()

        self.stop_button.setEnabled(False)

        self.__data = DataGatherer(1000, 0.1, 'danny')

    def __init_events(self):
        self.start_button.clicked.connect(self.__start_button)
        self.stop_button.clicked.connect(self.__stop_button)
        self.save_button.clicked.connect(self.__save_button)

    def __start_button(self):
        if not self._logging:
            self._logging = True
            self.start_button.setEnabled(False)
            self.stop_button.setEnabled(True)
            self.save_button.setEnabled(False)
            self.__data.start()
            print('Start button pressed')

    def __stop_button(self):
        if self._logging:
            self._logging = False
            self.start_button.setEnabled(True)
            self.stop_button.setEnabled(False)
            self.save_button.setEnabled(True)
            self.__data.stop()
            print('Stop button pressed')

    def __save_button(self):
        if not self._logging:
            self.__data.save()
            print('Save button pressed')

def main():
    app = QtWidgets.QApplication(sys.argv)
    form = MainProgram()
    form.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
