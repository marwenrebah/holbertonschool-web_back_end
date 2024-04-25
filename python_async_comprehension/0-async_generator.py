#!/usr/bin/env python3
 
import asyncio
from random import uniform

async def async_generator():
    for i in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
