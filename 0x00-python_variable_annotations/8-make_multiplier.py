#!/usr/bin/env python3
""" Complex types - functions"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    takes a float multiplier as argument,
    returns a function that multiplies a float by multiplier.
    """

    def multiplier_func(number: float) -> float:
        """multiplies a float by multiplier"""
        return number * multiplier

    return multiplier_func
