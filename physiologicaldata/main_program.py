from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
import sys
import signal
#import os
from PyQt5 import QtWidgets
#from PyQt5.QtWidgets import QFileDialog

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

        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(False)
        self.save_button.setEnabled(False)
        self.reset_all_button.setEnabled(False)
        self.reset_user_button.setEnabled(False)

        self.__data = DataGatherer(1000, 0.1)

    def __init_events(self):
        self.start_button.clicked.connect(self.__start_button)
        self.stop_button.clicked.connect(self.__stop_button)
        self.save_button.clicked.connect(self.__save_button)
        self.reset_all_button.clicked.connect(self.__reset_all_button)
        self.reset_user_button.clicked.connect(self.__reset_user_button)
        self.set_user_button.clicked.connect(self.__set_user_button)
        #self.set_path_button.clicked.connect(self.__set_path_button)

    def __start_button(self):
        if not self._logging:
            self._logging = True
            self.start_button.setEnabled(False)
            self.stop_button.setEnabled(True)
            self.save_button.setEnabled(False)
            self.__data.start()

    def __stop_button(self):
        if self._logging:
            self._logging = False
            self.start_button.setEnabled(True)
            self.stop_button.setEnabled(False)
            self.save_button.setEnabled(True)
            self.__data.stop()

    def __save_button(self):
        if not self._logging:
            self.__data.save()

    def __reset_all_button(self):
        self.__data.reset_all()

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
