#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Helper functions for AOC 2018."""

import codecs
import time
import sys

__author__ = "dddjjjbbb"
__version__ = "0.1"


def time_it(function):
    """Measure the execution time of a decorated function.

    To profile execution time, decorate method.

    :function: passed via decorator.
    :type name: str.
    :returns: execution time in ms.

    .. _url: https://bit.ly/2KYF8q7
    """
    def timed(*args, **kw):
        start_time = time.time()
        result = function(*args, **kw)
        end_time = time.time()
        if 'log_time' in kw:
            name = kw.get('log_name', function.__name__.upper())
            kw['log_time'][name] = int((start_time - end_time) * 1000)
        else:
            print('%r  %2.2f ms' %
                  (function.__name__, (end_time - start_time) * 1000))
        return result
    return timed


# @time_it
def read_lines_to_list(filename):
    """Read and append each line in a file to a list.

    :filename: Absolute path to file.
    :type name: str.
    :returns: List containing one object per line.
    :raises: For any I/O-related reason, e.g., "file not found" or "disk full".

    .. note::

    If a line contains leading or trailing whitespace, it will be removed.
    """
    try:
        with codecs.open(filename, 'r', encoding='utf-8') as f:
            content = f.readlines()
            return [line.strip() for line in content]
    except IOError as e:
        print('Could not read file ->', filename, '\nSee {}'.format(e))
        sys.exit()


def create_unique_list(string_list: ['ab', 'ab', 'abc']) -> ['ab', 'abc']:
    """Create a unique list for list.

    :string_list: List of strings.
    :type name: list.
    :returns: a unique list.
    :raises: If string_list input is empty.
    """
    if len(string_list) > 0:
        return list(set(string_list))
    sys.exit
    return 'List is empty'
