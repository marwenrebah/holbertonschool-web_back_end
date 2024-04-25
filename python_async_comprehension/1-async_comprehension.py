#!/usr/bin/env python3
"""Async Comprehension"""

from typing import List

aysnc_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """Collect 10 random numbers using an async comprehension."""
    return [i async for i in aysnc_generator()]
