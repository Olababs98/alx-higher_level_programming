#!/usr/bin/python3
"""Define a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
    """
    Initializes a Rectangle instance with a given width and height.

    Args:
        width (int): The width of the rectangle. Defaults to 0.
        height (int): The height of the rectangle. Defaults to 0.

    Raises:
        TypeError: If either width or height is not an integer.
        ValueError: If either width or height is less than 0.
    """
    self.width = width
    self.height = height

@property
def width(self):
    """
    Retrieves the width of the rectangle.

    Returns:
        int: The width of the rectangle.
    """
    return self.__width

@width.setter
def width(self, value):
    """
    Sets the width of the rectangle.

    Args:
        value (int): The new width of the rectangle.

    Raises:
        TypeError: If value is not an integer.
        ValueError: If value is less than 0.
    """
    if not isinstance(value, int):
        raise TypeError("width must be an integer")
    elif value < 0:
        raise ValueError("width must be >= 0")
    else:
        self.__width = value

@property
def height(self):
    """
    Retrieves the height of the rectangle.

    Returns:
        int: The height of the rectangle.
    """
    return self.__height

@height.setter
def height(self, value):
    """
    Sets the height of the rectangle.

    Args:
        value (int): The new height of the rectangle.

    Raises:
        TypeError: If value is not an integer.
        ValueError: If value is less than 0.
    """
    if not isinstance(value, int):
        raise TypeError("height must be an integer")
    elif value < 0:
        raise ValueError("height must be >= 0")
    else:
        self.__height = value

def area(self):
    """
    Calculates the area of the rectangle.

    Returns:
        int: The area of the rectangle.
    """
    return self.__width * self.__height

def perimeter(self):
    """
    Calculates the perimeter of the rectangle.

    Returns:
        int: The perimeter of the rectangle.
    """
    if self.__width == 0 or self.__height == 0:
        return 0
    else:
        return 2 * (self.__width + self.__height)
