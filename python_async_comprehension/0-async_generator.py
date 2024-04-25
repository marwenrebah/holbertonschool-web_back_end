#!/usr/bin/env python3
"""Async Generator"""

import asyncio
from random import uniform


async def async_generator():
    """Asynchronous generator function that yields random numbers with a 1-second delay."""
    for i in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
