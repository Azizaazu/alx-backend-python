#!/usr/bin/env python3
"""
Async Comprehension Module

contains a coroutine that collects 10 random numbers
using an async comprehension over async_generator.
"""


from typing import List
from importlib import import_module as using


async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collect 10 random numbers using an async comprehension.

    Returns:
        List[float]: List of 10 random numbers.
    """
    return [x async for x in async_generator()]
