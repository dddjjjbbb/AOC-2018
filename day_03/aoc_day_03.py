#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AOC day 3."""

import sys
import re
import itertools
from collections import Counter

sys.path.append("..")
try:
    from aoc_helpers.elves import time_it, read_lines_to_list
except ImportError as e:
    print('Please resolve import issue: {}'.format(e))
    sys.exit


__author__ = "dddjjjbbb"
__version__ = "'.'.1"


def create_fabric_matrix(rows, columns):
    """Create a matrix of n rows and m columns.

    :note: Visual epresentation of matrix for testing.
    :rows: Amount of rows.
    :type name: int.
    :columns: Amount of columns.
    :type name: int.
    :returns: A two-dimensional matrix.
    """
    return [['.'] * columns for i in range(rows)]


def get_dimensions(claims: ['#123 @ 3,2: 5x4']) -> [[123, 3, 2, 5, 4]]:
    """Get dimension data from each claim.

    :claims: list containing a string per claim.
    :type name: list.
    :returns: A list of lists containing id of claim and dimensions.
    ::raises: Currently no error handling.
    """
    dimensions = []
    claim_pattern = re.compile(r'((#)(\d+).*\s(\d+)(,)(\d+).*\s(\d+)(x)(\d+))')
    for claim in claims:
        matcher = re.search(claim_pattern, claim)
        if matcher:
            dimensions.append([matcher.group(3),  # claim_id
                               matcher.group(4),  # x
                               matcher.group(6),  # y
                               matcher.group(7),  # w
                               matcher.group(9)])  # h
    return [[int(n) for n in dimension] for dimension in dimensions]


def plot_claims_on_matrix(claims):
    # Omitting actual output in function annotation.
    # Cannot acurately illustrate ploting matrix (for obvious reasons).
    """Plot dimensions on matrix.

    :dimensions: A list of lists containing id of claim and dimensions.
    :type name: list.
    :returns: matrix post plot.
    ::raises: Currently no error handling.

    y
    |
    |
    |_____x

    """
    matrix = Counter()  # [Counter({'a': 2, 'c': 1}), Counter({'d': 3})]
    for claim in claims:
        claim_id, x, y, w, h = claim  # unpack claim.
        for fabric_x_axis in range(x, x + w):
            for fabric_y_axis in range(y, y + h):
                matrix[fabric_x_axis, fabric_y_axis] += 1
    return matrix


def calculate_claims_within_two_or_more_claims(plotted_matrix):
    """Calculate claims within two or more claims.

    :plotted_matrix: A matrix with claims plotted.
    :type name: dict subclass for counting hashable objects.
    :returns: amount of overlapping claims.
    ::raises: Currently no error handling.
    # Answer 104712
    """
    matrix = plotted_matrix
    counter = itertools.count(1)
    overlapping = [(next(counter), n) for n in matrix.values() if n > 1]
    return int(overlapping[-1][0])


@time_it
def main():
    """Main entry point for module."""
    _input = read_lines_to_list(r'input.txt')
    dimensions = get_dimensions(_input)
    plotter = plot_claims_on_matrix(dimensions)
    answer_part_1 = calculate_claims_within_two_or_more_claims(plotter)
    print(answer_part_1)


if __name__ == '__main__':
        main()
