#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A Fibo Generator."""


def xfibo(count):
    """Fibo sequence generation function.

    Args:
        count (int): Number of integers to return in the sequence.

    Returns:
        generator: A generated number of the fibo sequence.

    Examples:
        >>> for x in xfibo(5):
                print x

        0
        1
        1
        2
        3
    """
    mycounter = 0
    lastnum, curnum = 0, 1
    while mycounter < count:
        yield lastnum
        lastnum, curnum = curnum, lastnum + curnum
        mycounter += 1
