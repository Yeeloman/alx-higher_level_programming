#!/usr/bin/python3

class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        a = not isinstance(value, int)
        b = len(value) != 2
        c = not all(isinstance(num, int) for num in value)
        d = not all(num >= 0 for num in value)
        if a or b or c or d:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            [print("") for i in range(self.__position[1])]
            sqr_pattern = " " * self.__position[0] + "#" * self.__size + "\n"
            print(sqr_pattern * self.__size, end="")
