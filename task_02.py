#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A Fibo Generator."""


import task_01


def fibo(count):
    """Creates a list of a Fibo sequence.

    Args:
        count (int): Number of integers to return in the sequence.

    Returns:
        list: A list of numbes in fibo sequence.

    Examples:
        >>> fibo(5)
        [0, 1, 1, 2, 3]
        >>> fibo(10)
        [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    """
    return [x for x in task_01.xfibo(count)]
