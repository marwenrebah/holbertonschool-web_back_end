#!/usr/bin/env python3
"""Mixed list"""

from typing import List
from typing import Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a mixed list of integers and
    floats and return the result as a float.
    """
    return sum(mxd_lst)
