#!/usr/bin/env python3
"""
Module for converting a string and an int or float to a tuple.
"""

from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Convert a string and an int or float to a tuple.
    Args:
        k (str): The string key.
        v (Union[int, float]): The int or float value.
    Returns:
        Tuple[str, float]: A tuple containing the string key and the square of the int/float value.
    """
    return (k, v ** 2)
