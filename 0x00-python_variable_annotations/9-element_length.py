#!/usr/bin/env python3
""" annotated version of the element_length function """


from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of each element in the input list.

    Args:
        lst (Iterable[Sequence]): The input list

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples
    """
    return [(i, len(i)) for i in lst]
