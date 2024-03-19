#!/usr/bin/env python3

"""
Measure Runtime Module
that executes async_comprehension four times in parallel
using asyncio.gather and measures the total runtime.
"""


import asyncio
from typing import List
from async_comprehension import async_comprehension


async def measure_runtime() -> float:
    """
    Measure total runtime of executing async_comprehension
    Returns:
        float: Total runtime in seconds.
    """
    start_time = asyncio.get_running_loop().time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = asyncio.get_running_loop().time()
    return end_time - start_time
