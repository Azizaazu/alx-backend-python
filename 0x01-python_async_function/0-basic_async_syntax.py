#!/usr/bin/env python3

"""
This module provides a basic asynchronous coroutine.
"""

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """
    An asynchronous coroutine that waits for a random delay
    """
	wait_time = random.random() * max_delay
	await asyncio.sleep(wait_time)
	return wait_time
