from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
import thread
import time

from logger import DataLogger
from device_interface import DeviceInterface

class DataGatherer(object):
    _COLUMNS = ['emotion', 'bpm', 'gaze-x', 'gaze-y']

    _logging = False

    def __init__(self, limit, rate, name):
        self._limit = limit
        self._rate = rate
        self.__data_log = DataLogger(
            self._limit,
            columns=self._COLUMNS,
            path='/home/danny/Desktop/users/{}'.format(name)
        )
        self.__device_interface = DeviceInterface()

        try:
            thread.start_new_thread(self.__thread_data, ('Thread-1', self._rate))
        except Exception as e:
            print(e)

    def __thread_data(self, thread_name, rate):
        while True:
            if self._logging:
                time.sleep(rate)
                #print(thread_name)
                self.__device_interface.get_data(self._data)

    def _data(self, data):
        self.__data_log.log(data)

    def start(self):
        self._logging = True

    def stop(self):
        self._logging = False

    def save(self):
        self.__data_log.save()

    def reset_all(self):
        pass

    def reset_session(self):
        pass

    def reset_user(self):
        pass

    def get_user(self):
        pass

    def set_user(self):
        pass

def main():
    """Runs as main if python file is not imported
    """

    pass

if __name__ == '__main__':
    main()
