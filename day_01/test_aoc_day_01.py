#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests for AOC day 01."""

import pytest
from aoc_day_01 import remove_non_ints_from_list
from aoc_day_01 import list_of_strings_to_int
from aoc_day_01 import what_is_the_frequency_kenneth
from aoc_day_01 import frequency_calibrator

__author__ = "dddjjjbbb"
__version__ = "0.1"


@pytest.mark.parametrize(
    'test_input, expected_output',
    [(['Testing', '+1', '-23'], ['+1', '-23']),
     (['Testing', '+1', '-23'], ['+1', '-23'])]
)
def test_removing_non_int_from_list(test_input, expected_output):
    """Test removing object not of type int from list."""
    assert remove_non_ints_from_list(test_input) == expected_output


def test_removing_non_int_from_empty_list():
    """Test removing object not of type int from empty list."""
    error_on_empty = 'List is empty, please review values.'
    assert remove_non_ints_from_list([]) == error_on_empty


@pytest.mark.parametrize(
    'test_input, expected_output',
    [(['+1', '-23'], [+1, -23]),
     (['+7', '+7', '-2', '-7', '-4'], [+7, +7, -2, -7, -4])]
)
def test_casting_string_list_to_int_list(test_input, expected_output):
    """Test casting each string in list to int."""
    assert list_of_strings_to_int(test_input) == expected_output


@pytest.mark.parametrize(
    'test_input, expected_output',
    [(['+1', '-2', 'foo', '-21'],
        'Please check string "foo" at index 2 in the list.'),
     (['-3bar', '-1', '-2'],
      'Please check string "-3bar" at index 0 in the list.')])
def test_error_handling_casting_string_to_int(test_input, expected_output):
    """Test meaningful error is thrown when casting string to int."""
    assert list_of_strings_to_int(test_input) == expected_output


@pytest.mark.parametrize(
    'test_input, expected_output',
    [([+1, -2, +3, +1], 3),
     ([+1, +1, +1], 3),
     ([+1, +1, -2], 0),
     ([-1, -2, -3], -6)])
def test_getting_total_frequency(test_input, expected_output):
    """Test summing all numbers in list."""
    assert what_is_the_frequency_kenneth(test_input) == expected_output


@pytest.mark.parametrize(
    'test_input, expected_output',
    [([+1, -1], 0),
     ([+3, +3, +4, -2, -4], 10),
     ([-6, +3, +8, +5, -6], 5),
     ([+7, +7, -2, -7, -4], 14)])
def test_frequency_calibration(test_input, expected_output):
    """Test calculating the first value that is reached twice."""
    assert frequency_calibrator(test_input) == expected_output


if __name__ == '__main__':
    pytest.main()
