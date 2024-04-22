#!/usr/bin/env python3
""" Multiplier """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable:
    """
    Creates a function that multiplies a number by a given multiplier.
    """
    def multiplier_function(value: float) -> float:
        """
        Multiplies a number by the given multiplier.
        """
        return value * multiplier

    return multiplier_function
