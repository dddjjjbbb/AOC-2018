#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AOC day 01."""

import sys
import re
from itertools import cycle

sys.path.append("..")
try:
    from aoc_helpers.elves import time_it, read_lines_to_list
except ImportError as e:
    print('Please resolve import issue: {}'.format(e))
    sys.exit

__author__ = "dddjjjbbb"
__version__ = "0.1"


# @time_it
def remove_non_ints_from_list(string_list):
    """Filter list of strings containing non integers.

    :string_list: List of strings.
    :type name: list.
    :returns: all strings that are non integers.
    :raises: If the filtered list is empty.
    """
    original_length = len(string_list)
    int_regex = re.compile(r'([^a-zA-Z]\d+)')
    numeric_strings = list(filter(int_regex.search, string_list))
    # Remove strings that potentially contain trailing text.
    # pattern = re.compile(r'([^a-zA-Z]\d+)(.+)')
    # numeric_strings = [(re.sub(pattern, x)) for x in numeric_strings]
    strings_removed = int(original_length - len(numeric_strings))
    if numeric_strings:
        if strings_removed == 1:
            print('{} string was removed.'.format(strings_removed))
        else:
            if strings_removed > 1:
                print('{} strings removed'.format(strings_removed))
        return numeric_strings
    return 'List is empty, please review values.'


# @time_it
def list_of_strings_to_int(string_list):
    """Convert each string in list to int.

    :string_list: List of strings.
    :type name: list.
    :returns: Each string in string list as an integer.
    :raises: If a string in the list cannot be cast, a ValueError is thrown.
    The user is shown the value in question and the corrsponding index.
    """
    int_list = []
    for index, value in enumerate(string_list):
        try:
            int_list.append(int(value))
        except ValueError:
            sys.exit
            return 'Please check string "{}" at index {}.'.format(value, index)
    return int_list


# @time_it
def what_is_the_frequency_kenneth(int_list):
    """Calculate the sum of all numbers in list.

    :int_list: List of integers.
    :type name: list.
    :returns: Sum total after summing.
    """
    return sum(int_list)


@time_it
def frequency_calibrator(int_list):
    """Calculate the first value reached twice.

    e.g +1, -1 first reaches 0 twice.

    :int_list: List of integers.
    :type name: list.
    :returns: The first value that is reached twice.

    .. warning::

    Current iteration over loop is indefinite.

    # TODO Stop iteration after 10000 passes.
    """
    frequency = 0
    frequency_set = set()
    frequency_set.add(0)
    """
    .. warning::

    0 must be added to the set, prior to the loop.
    Without doing so, this input [+1, -1] would evaluate to 1.
    """
    indefinite_loop = cycle(int_list)
    for n in indefinite_loop:
        frequency = frequency + n
        if frequency in frequency_set:
            return frequency
        else:
            frequency_set.add(frequency)


@time_it
def main():
    """Main entry point for module."""
    _input = read_lines_to_list(r'input.txt')
    filtered_strings = remove_non_ints_from_list(_input)
    converted_to_ints = list_of_strings_to_int(filtered_strings)
    frequency_result = what_is_the_frequency_kenneth(converted_to_ints)
    print('The total frequency is: {}'.format(frequency_result))
    calibrator_result = frequency_calibrator(converted_to_ints)
    print('The calibrated frequency is: {}'.format(calibrator_result))


if __name__ == '__main__':
        main()
