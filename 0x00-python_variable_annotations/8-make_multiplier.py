#!/usr/bin/env python3
"""
Module for creating a multiplier function.
"""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Return a function that multiplies a float by the given multiplier.
    Args:
        multiplier (float): The multiplier value.
    Returns:
        Callable[[float], float]: A function that takes a float and returns the product.
    """
    def multiplier_func(x: float) -> float:
        """
        Multiply a float by the given multiplier.
        Args:
            x (float): The input float.
        Returns:
            float: The product of x and the multiplier.
        """
        return x * multiplier
    return multiplier_func
