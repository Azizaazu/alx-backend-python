#!/usr/bin/env python3
""" Given the parameters and the return values"""


from typing import Any, TypeVar, Mapping, Union


T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    """
    Get the value associated with the key in the dictionary safely.
    """
    if key in dct:
        return dct[key]
    else:
        return default
