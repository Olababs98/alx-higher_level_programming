#!/usr/bin/python3
"""Define a Rectangle class."""


class Rectangle:
    """
    Class that defines a rectangle.
    """
    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle instance with an optional width and height.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieves the width of the rectangle instance.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle instance.
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
        Retrieves the height of the rectangle instance.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle instance.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Returns the area of the rectangle instance.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Returns the perimeter of the rectangle instance.
        """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)
