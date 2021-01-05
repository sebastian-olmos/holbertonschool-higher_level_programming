#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Class named Square with a private instace attribute
"""


class Square:
    """Definition of a Square
    """
    def __init__(self, size=0):
        """Instantiate a Square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Current square area
        """
        return self.__size ** 2
