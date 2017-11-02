# Compatability Imports
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import random


def min_max_normalization(dataframe):
    """

    Args:
        dataframe: The dataframe that contains all data to be normalized.

    Returns:
        A `Dataframe` that contains the normalized data.
        
    """

    return (dataframe - dataframe.mean()) / (dataframe.max() - dataframe.min())


def q_generator():
    while True:
        q_type = random.randint(0, 6)
        q_conf = random.random()
        
        yield q_type, q_conf
