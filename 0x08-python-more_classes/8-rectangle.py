#!/usr/bin/python3
"""Define a Rectangle class."""


class Rectangle:
    """
    Rectangle class with attributes width and height, and methods area and
    perimeter. Includes class attributes to keep track of the number of
    instances and the symbol to use for string representation.
    """


    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle object with a given width and height.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """
        Returns a string representation of a Rectangle object using the '#'
        symbol.
        """
        if self.width == 0 or self.height == 0:
            return ""
        else:
            return (str(self.print_symbol) * self.width + "\n") * self.height

    def __repr__(self):
        """
        Returns a string representation of a Rectangle object that can be used
        to create a new instance of the object using the 'eval()' function.
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """
        Deletes a Rectangle object and prints a message indicating that the
        object has been deleted.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """
        Getter method for the width attribute.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width attribute.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Getter method for the height attribute.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height attribute.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Returns the area of a Rectangle object.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Returns the perimeter of a Rectangle object.
        """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (self.width + self.height) * 2
    def __str__(self):
        # check if width or height is 0
        if self.width == 0 or self.height == 0:
            # return an empty string
            return ""
        # return the string representation of the rectangle
        else:
            return "\n".join([str(self.print_symbol) * self.width] * self.height)

    # repr method
    def __repr__(self):
        # return the string representation of the rectangle to recreate a new instance
        return f"Rectangle({self.width}, {self.height})"

    # delete method
    def __del__(self):
        # decrement the instance counter
        Rectangle.number_of_instances -= 1
        # print the deletion message
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        # check if rect_1 is an instance of Rectangle
        if not isinstance(rect_1, Rectangle):
            # raise TypeError
            raise TypeError("rect_1 must be an instance of Rectangle")
        # check if rect_2 is an instance of Rectangle
        elif not isinstance(rect_2, Rectangle):
            # raise TypeError
            raise TypeError("rect_2 must be an instance of Rectangle")
        # return the Rectangle object with the bigger or equal area
        else:
            if rect_1.area() >= rect_2.area():
                return rect_1
            else:
                return rect_2
