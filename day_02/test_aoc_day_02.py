#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests for AOC day 02."""

import pytest

from aoc_day_02 import splitter
from aoc_day_02 import calculate_checksum
from aoc_day_02 import create_unique_list
from aoc_day_02 import find_ids_differing_by_one_char


__author__ = "dddjjjbbb"
__version__ = "0.1"


def test_splitting_array_into_componants():
    """Test splitting array into componants."""
    assert splitter(['abbcde']) == [['a', 'b', 'b', 'c', 'd', 'e']]


def test_splitting_array_into_componants_where_empty():
    """Test splitting array into componants where empty."""
    assert splitter([]) == 'List is empty'


def test_counting_one_for_any_duplicates_occuring_more_than_once():
    """Test counting duplicates that occur more than once."""
    test_dict = [dict(b=3, a=2, c=1)]
    assert calculate_checksum(test_dict) == 1


def test_creating_unique_list():
    """Test creating unique list."""
    test_list = ['abcde', 'abcde', 'abcdf']
    assert create_unique_list(test_list) == ['abcde', 'abcdf']


def test_find_string_that_differs_by_one_char_in_same_position():
    """Testing finding string that differs by one char in same position."""
    test_list = ['abcde', 'abcdf']
    assert find_ids_differing_by_one_char(test_list) == 'abcd'


if __name__ == '__main__':
    pytest.main()
