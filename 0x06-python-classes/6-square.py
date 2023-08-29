#!/usr/bin/python3
"""square class"""


class Square:
    """square class"""
    def __init__(self, size=0, position=(0, 0)):
        """init square
        Args:
            size (int): square size.
            position (int, int): The position of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Sets value into size, must be int.

        Args:
            value (int): square size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets value into size, must be int.

    Args:
    value (int): square size.
    """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Sets value of position.

        Args:
            value (int): square position.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets value into position.

        Args:
            value (int): square position.
        """
        a = not isinstance(value, int)
        b = len(value) != 2
        c = not all(isinstance(num, int) for num in value)
        d = not all(num >= 0 for num in value)
        if a or b or c or d:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """calc area
        returns:
            return area.
        """
        return self.__size * self.__size

    def my_print(self):
        """prints in stdout the square with #"""
        if self.__size == 0:
            print("")
        else:
            [print("") for i in range(self.__position[1])]
            sqr_pattern = " " * self.__position[0] + "#" * self.__size + "\n"
            print(sqr_pattern * self.__size, end="")