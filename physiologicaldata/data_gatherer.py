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

    def __init__(self, limit, rate):
        """Initializes DataGatherer.

        Data logger and device interface are initialized.
        """

        self._limit = limit
        self._rate = rate
        self._path = 'user_data' # '/home/danny/Desktop/user_data'
        self._user = None
        self._device_data = None
        self._device_status = None
        self.__data_log = None
        self.__device_interface = DeviceInterface()

        # Start thread on thread_data method with name Thread-1
        try:
            thread.start_new_thread(self.__thread_data, ('Thread-1', self._rate))
        except Exception as e:
            print(e)

    def __set_data_logger(self):
        """Initializes data logger
        """

        if self._user is None or self._path is None:
            print('Set user and path!')
            return

        if self.__data_log is not None:
            self.__data_log = None

        self.__data_log = DataLogger(
            self._limit,
            columns=self._COLUMNS,
            path='{}/{}'.format(self._path, self._user)
        )

    def __thread_data(self, thread_name, rate):
        """Thread method to capture data from device interface.
        """

        while True:
            time.sleep(rate) # controls the data logging rate

            self.__device_interface.get_status(self._device_status_callback)

            if self._logging:
                #print(thread_name)
                self.__device_interface.get_data(self._device_data_callback)

    def _device_data_callback(self, data):
        """_device_data_callback is a callback method for the device interface.
        """

        self._device_data = data
        self.__data_log.log(data)

    def _device_status_callback(self, status):
        """_device_status_callback is a callback method for the device interface.
        """

        self._device_status = status

    def get_data(self, data_callback):
        """Gets data from the device interface.

        Data is retrieved from Device Interface. This array is passed as an
        argument to the 'data' callback function.

        Args:
            data (function): Callback function with array parameter.
        """

        data_set = []

        if self._logging:
            data_set = self._device_data
        else:
            data_set = ['N/A', 'N/A', 'N/A', 'N/A']

        data_callback(data_set, self._device_status)

    def start(self):
        """Start user data logging.

        Logging is set to true for the thread method to start logging.
        """

        if self.__data_log is None:
            print('User or path not set!')
            return

        self._logging = True

    def stop(self):
        """Stop user data logging.

        Logging is set to false for the thread method to stop logging.
        """

        if self.__data_log is None:
            print('User or path not set!')
            return

        self._logging = False

    def save(self):
        """Saves user data.
        """

        if self.__data_log is None:
            print('User or path not set!')
            return

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

    def reset_user(self):
        """Resets logged data for the specified user.

        The directory for the specified user is deleted if the user exists.

        Args:
            user (string): Specifies the name of the user.
        """

        if self._user is None:
            print('User not set!')
            return

        if not os.path.isdir(self._path):
            print('No users.')
            return

        user_path = '{}/{}'.format(self._path, self._user)
        if not os.path.isdir(user_path):
            print('User does not exist.')
            return

        print('Deleting user {}'.format(self._user))
        shutil.rmtree(user_path)

    def get_user(self):
        """Gets the current user.
        """

        pass

    def set_user(self, user):
        """Sets the current user.

        Set the current user to log data for.

        Args:
            user (string): Specifies the name of the user.
        """

        if user is '' or user is None or not user:
            print('Invalid user!')
            return

        print('User set')

        self._user = user
        self.__set_data_logger()

    '''
    def set_path(self, path):
        """Sets the data path directory.

        Set the path in which the data will be saved in.

        Args:
            path (string): Specifies the path of the data.
        """

        print('Path set')

        self._path = '{}/user_data'.format(path)

        if self._user is not None and self._path is not None:
            self.__set_data_logger()
    '''

def main():
    """Runs as main if python file is not imported
    """

    pass

if __name__ == '__main__':
    main()
