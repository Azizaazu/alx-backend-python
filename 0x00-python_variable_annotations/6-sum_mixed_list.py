#!/usr/bin/env python3
"""
Module for summing a mixed list of integers and floats.
"""

from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sum a mixed list of integers and floats and return their sum.
    Args:
        mxd_lst (List[Union[int, float]]): The mixed list of integers and floats.
    Returns:
        float: The sum of the mixed list.
    """
    return sum(mxd_lst)
