"""Log user data

This module logs data from the device interface for specified users. Users
can be added by logging data for that user and deleted by reseting all users
or one particular user.
"""

from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
import thread
import os
import shutil
import time

from logger import DataLogger
from device_interface import DeviceInterface

class DataGatherer(object):
    """Data Gatherer manages user data logging.

    A folder is created for all users and named after each user. A thread
    is then initalized to capture data from the device interface. This data
    is logged into csv files relative to its intended user.

    Args:
            limit (int): Specifies the logging limit.
            rate (int): Specifies the logging rate.
            name (str): Contains name of user.
    """

    _COLUMNS = ['emotion', 'bpm', 'Gx', 'Gy']

    _logging = False

    def __init__(self, limit, rate, name):
        """Initializes DataGatherer.

        Data logger and device interface are initialized.
        """

        self._limit = limit
        self._rate = rate
        self._path = '/home/danny/Desktop/users'
        self.__data_log = DataLogger(
            self._limit,
            columns=self._COLUMNS,
            path='{}/{}'.format(self._path, name)
        )
        self.__device_interface = DeviceInterface()

        # Start thread on thread_data method with name Thread-1
        try:
            thread.start_new_thread(self.__thread_data, ('Thread-1', self._rate))
        except Exception as e:
            print(e)

    def __thread_data(self, thread_name, rate):
        """Thread method to capture data from device interface.
        """

        while True:
            if self._logging:
                time.sleep(rate) # controls the data logging rate
                #print(thread_name)
                self.__device_interface.get_data(self._data)

    def _data(self, data):
        """_data is a callback method for the device interface.
        """

        self.__data_log.log(data)

    def start(self):
        """Start user data logging.

        Logging is set to true for the thread method to start logging.
        """

        self._logging = True

    def stop(self):
        """Stop user data logging.

        Logging is set to false for the thread method to stop logging.
        """
        self._logging = False

    def save(self):
        """Saves user data.
        """

        self.__data_log.save()

    def reset_all(self):
        """Resets logged data for all users.

        All user directories are deleted if users exist.
        """

        if not os.path.isdir(self._path):
            print('No users.')
            return

        print('Deleting all users.')
        user_dirs = os.listdir(self._path)
        for folder in user_dirs: # delete all existing user directories
            shutil.rmtree('{}/{}'.format(self._path, folder))


    def reset_session(self):
        """Resets users current logged session
        """

        pass

    def reset_user(self, user):
        """Resets logged data for the specified user.

        The directory for the specified user is deleted if the user exists.

        Args:
            user (string): Specifies the name of the user.
        """

        if not os.path.isdir(self._path):
            print('No users.')
            return

        user_path = '{}/{}'.format(self._path, user)
        if not os.path.isdir(user_path):
            print('User does not exist.')
            return

        print('Deleting user {}'.format(user))
        shutil.rmtree(user_path)

    def get_user(self):
        """Gets the current user.
        """

        pass

    def set_user(self):
        """Sets the current user.
        """

        pass

def main():
    """Runs as main if python file is not imported
    """

    pass

if __name__ == '__main__':
    main()
