"""Log data into csv files

This module uses dictionary data to log into data frames. The data frames are
then used to save the data into time-stamped csv files inside time-stamped
folders of the current session.
"""

from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
import os
import datetime
import pandas as pd

class DataLogger(object):
    """Data Logger manages data logging into csv files.

    A folder is created for every session named after the system time. CSV files
    are then saved inside said folder. If data exceeds the specified logging
    limit, the CSV file is saved and a new CSV file is created.

    Args:
            limit (int): Specifies the logging limit. Defaults to 1000 if
                parameter not specified.
            columns (dict): A dictionary of strings for the header of the
                dataframe.
            path (str): Contains the path directory for the data.
    """

    def __init__(self, limit=1000, columns=None, path=os.path.expanduser('~')):
        """Initializes DataLogger.

        Columns dictionary and data frame are initialized.
        """

        if not columns:
            raise ValueError('\'columns\' argument is empty.')

        self._log_limit = limit
        self._log_count = 0 # keeps count of logging attempts
        self._columns = ['timestamp'] + columns
        self._path = path
        self.__df = pd.DataFrame({}, columns=self._columns)

        print('Data Log initialized')

    def __datestamp(self):
        """Formats system date time to string.
        """

        return '{:%Y-%m-%d %H:%M:%S.%f}'.format(datetime.datetime.now())

    def log(self, data):
        """Logs the data to the data frame.

        A data set is created using a header dictionary, along with a timestamp.

        Args:
            data (dictionary): Contains a dictionary of strings.
        """

        if self.__df is None: # Reinitialize the dataframe if it's None
            self.__df = pd.DataFrame({}, columns=self._columns)
            print('New dataframe initialized')

        if not data:
            raise ValueError('\'data\' argument is empty.')

        if len(self._columns)-1 is not len(data):
            raise RuntimeError('Size of \'data\' does not match size of \'columns\'.')

        # When logging count exceeds the specified logging limit, the current data
        # data frame is saved into a csv file and the data frame is re-initialized.
        # The logging count is then reset to 0.
        if self._log_count >= self._log_limit:
            self.save()
            self.__df = pd.DataFrame({}, columns=self._columns)
            self._log_count = 0

        timestamp = self.__datestamp()
        raw_data = {'timestamp': [timestamp]}

        for i in range(len(data)):
            raw_data[self._columns[i+1]] = [data[i]]

        # initialize new data frame wiht raw data to append to current data frame
        dft = pd.DataFrame(raw_data, columns=self._columns)
        self.__df = self.__df.append(dft, ignore_index=True)

        self._log_count += 1

    def save(self):
        """Saves the data frame into a csv file

        A folder is first created if it doesn't exist. The data frame is then
        saved into a csv file inside said folder.
        """

        if not os.path.isdir(self._path):  # create folder if nonexistent
            os.makedirs(self._path)

        # specify name and file path and save to csv
        d_file = '{}/{}.csv'.format(self._path, self.__datestamp())
        self.__df.to_csv(d_file)
        self.__df = None

        print('Data log saved')

def main():
    """Runs as main if python file is not imported
    """

    pass

if __name__ == '__main__':
    main()
