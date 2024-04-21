#!/usr/bin/env python3

""" mixed list """
from typing import Union, List


def sum_mixed_list(mixed: List[Union[int, float]]) -> float:
    """returns sum as a float."""
    return float(sum(mixed))
