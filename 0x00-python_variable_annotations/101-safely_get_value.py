#!/usr/bin/env python3
""" Given the parameters and the return values"""


from typing import Dict, TypeVar, Optional


KT = TypeVar('KT')
VT = TypeVar('VT')


def safely_get_value(dct: Dict[KT, VT], key: KT, default: Optional[VT] = None) -> Optional[VT]:
    """
    Get the value associated with the key in the dictionary safely.

    Args:
        dct (Dict[KT, VT]): The input dictionary.
        key (KT): The key to search for in the dictionary.
        default (Optional[VT], optional): The default value to return.

    Returns:
        Optional[VT]: The value associated with the key, otherwise the default.
    """
    if key in dct:
        return dct[key]
    else:
        return default
