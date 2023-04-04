#!/usr/bin/python3
"""Define a Rectangle class."""


class Rectangle:
    """Class that defines a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance with optional width and height"""

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter method for width"""

        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter method for height"""

        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Calculate the area of the rectangle"""

        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the rectangle"""

        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        """Return a string representation of the rectangle"""

        if self.width == 0 or self.height == 0:
            return ""
        else:
            return (str(self.print_symbol) * self.width + "\n") * self.height

    def __repr__(self):
        """Return a string representation of the rectangle"""

        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Print a message when the instance is deleted"""

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
