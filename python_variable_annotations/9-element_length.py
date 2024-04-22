#!/usr/bin/env python3
""" Let's duck type an iterable object """

from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    Returns a list of tuples containing elements from the
    input list and their lengths.
    """
    return [(i, len(i)) for i in lst]
