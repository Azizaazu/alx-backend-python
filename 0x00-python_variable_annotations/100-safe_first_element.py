#!/usr/bin/env python3
""" annotated version of the safe_first_element function """


from typing import Any, List, Union


def safe_first_element(lst: List[Any]) -> Union[Any, None]:
    """
    Return the first element of the list if it exists, or None.
    Args:
        lst (List[Any]): The input list.
    Returns:
        Union[Any, None]: The first element of the list or None.
    """
    if lst:
        return lst[0]
    else:
        return None
