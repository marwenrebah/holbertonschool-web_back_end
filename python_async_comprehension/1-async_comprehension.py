#!/usr/bin/env python3
"""Async Comprehension"""

aysnc_generator = __import__("0-async_generator").async_generator

import asyncio
from typing import List


async def async_comprehension() -> List[float]:
    """Collect 10 random numbers using an async comprehension."""
    return [i async for i in aysnc_generator()]
