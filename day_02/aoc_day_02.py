#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AOC day 02."""

import sys
from collections import Counter
import itertools

sys.path.append("..")
try:
    from aoc_helpers.elves import (time_it,
                                   read_lines_to_list,
                                   create_unique_list)
except ImportError as e:
    print('Please resolve import issue: {}'.format(e))
    sys.exit

__author__ = "dddjjjbbb"
__version__ = "0.1"


def splitter(string_list: ['abbcde']) -> [['a', 'b', 'b', 'c', 'd', 'e']]:
    """Split string_list into list of lists.

    For each item/line in string list.
    split componant letters into their own list.

    :string_list: List of strings.
    :type name: list.
    :returns: a list of lists, where each list contains each letter.
    :raises: If the filtered list is empty.
    """
    if len(string_list) > 0:
        return [list(x) for x in string_list]
    sys.exit
    return 'List is empty'


def count_occurance_of_each_letter(list_of_lists: [['a', 'a', 'c'], ['d', 'd', 'd']]) -> [Counter({'a': 2, 'c': 1}), Counter({'d': 3})]:
    """Create a list of dictionaries containing:
    key: letter
    value: frequency occurance

    :list_of_lists: A list of strings.
    :type name: list (nested).
    :returns: a list of dictionaries.
    :raises: Currently no error handling.
    """
    dicts = []
    for _list in list_of_lists:
        dicts.append((Counter(_list)))
    return dicts


def calculate_checksum(counter_dicts: [Counter({'a': 2, 'c': 1}), Counter({'d': 3})]) -> 1:
    exactly_two = 0
    exactly_three = 0
    for _dict in counter_dicts:
        _dict = _dict.values()
        if 2 in _dict:
            exactly_two += 1
        if 3 in _dict:
            exactly_three += 1
    return exactly_two * exactly_three


def find_ids_differing_by_one_char(string_list: ['abcde', 'abcdf']) -> 'abcd':
    """Find strings in list that differ by one character alone.

    Given a list of strings of equal length.
    Returns string to user with differing character removed.
    :string_list: List of strings.
    :type name: list.
    :returns: string with offending character removed.
    :raises:

    """
    """
    Calculating binomial coefficient.
    Given an input where n = 250 and r = 2 (max = 31125 iterations)
    The number of items returned is:
    n! / r! / (n-r)! when 0 <= r <= n or zero when r > n.
    """
    for a, b in itertools.combinations(create_unique_list(string_list), 2):
        """
        generating an index list for each combination, where values differ.
        ['axcd', 'abcc'] would return [1, 3], as the values at those indexes
        differ.
        """
        diff_cal = [char for char in range(len(a)) if a[char] != b[char]]
        """Checking values are identical and contain a single element."""
        if diff_cal.count(diff_cal[0]) == len(diff_cal):
            """Converting integer list to int."""
            index = int(''.join(map(str, diff_cal)))
            """
            Removing character at index.
            Syntax: foo.replace(foo[index], new, count)
            The count parameter is max replacements (in our case, 1)
            """
            return a.replace(a[index], '', 1)


@time_it
def main():
    """Main entry point for module."""
    _input = read_lines_to_list(r'input.txt')
    # Part One
    _list_of_lists = splitter(_input)
    counter = count_occurance_of_each_letter(_list_of_lists)
    checksum = calculate_checksum(counter)
    print(checksum)
    # Part Two
    common_letters_in_box_ids = find_ids_differing_by_one_char(_input)
    print(common_letters_in_box_ids)


if __name__ == '__main__':
        main()
