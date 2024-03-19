#!/usr/bin/env python3

"""
Measure Runtime Module
that executes async_comprehension four times in parallel
using asyncio.gather and measures the total runtime.
"""


import asyncio
import time
from importlib import import_module as using


async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure total runtime of executing async_comprehension
    Returns:
        float: Total runtime in seconds.
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time_time() - start_time
