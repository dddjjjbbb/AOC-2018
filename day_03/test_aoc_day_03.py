#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests for AOC day 03."""

import pytest
from aoc_day_03 import create_fabric_matrix
from aoc_day_03 import get_dimensions
from aoc_day_03 import calculate_claims_within_two_or_more_claims

__author__ = "dddjjjbbb"
__version__ = "0.1"


def test_creating_3d_fabric_array():
    """Test length of matrix is correct after creation."""
    assert sum(len(x) for x in create_fabric_matrix(100, 100)) == 10000


def test_getting_dimension_from_claim():
    """Test dimensions are correctly returned from claim."""
    assert get_dimensions(['#123 @ 3,2: 5x4']) == [[123, 3, 2, 5, 4]]


def test_dimensions_overlap():
    """Test calculation function returns correct amount of overlaps."""
    claims = [[1, 1, 3, 4, 4], [2, 3, 1, 4, 4], [3, 5, 5, 2, 2]]
    assert calculate_claims_within_two_or_more_claims(claims) == 4


if __name__ == '__main__':
    pytest.main()
