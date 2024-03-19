#!/usr/bin/env python3

"""
Async Generator Module
contains an asynchronous generator coroutine
that yields random numbers between 0 and 10.
"""


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Generate random numbers asynchronously.

    This coroutine loops 10 times

    Yields:
    float: Random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
