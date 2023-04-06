#!/usr/bin/python3
"""Define an integer addition function"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int/float): The first number.
        b (int/float): The second number. Defaults to 98.

    Returns:
        int: The sum of a and b.

    Raises:
        TypeError: If a or b are not integers or floats.

    """

    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer or float')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer or float')

    return int(a) + int(b)
