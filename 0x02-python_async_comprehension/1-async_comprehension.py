#!/usr/bin/env python3
"""
Async Comprehension Module

contains a coroutine that collects 10 random numbers
using an async comprehension over async_generator.
"""


import asyncio
from typing import List
from async_generator import async_generator


async def async_comprehension() -> List[int]:
    """
    Collect 10 random numbers using an async comprehension.

    Returns:
        List[int]: List of 10 random numbers.
    """
    return [x async for x in async_generator()]
