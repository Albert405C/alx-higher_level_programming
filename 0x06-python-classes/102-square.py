#!/usr/bin/python3
class Square:
    """
    This class defines a square
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Parameters:
            value (float or int): The size to be set.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            float or int: The area of the square.
        """
        return self.size ** 2

    def __eq__(self, other):
        """
        Equality comparator for two Square instances based on area.

        Parameters:
            other (Square): The other Square instance for comparison.

        Returns:
            bool: True if areas are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Inequality comparator for two Square instances based on area.

        Parameters:
            other (Square): The other Square instance for comparison.

        Returns:
            bool: True if areas are not equal, False otherwise.
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """
        Greater than comparator for two Square instances based on area.

        Parameters:
            other (Square): The other Square instance for comparison.

        Returns:
            bool: True if area is greater, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Greater than or equal to comparator for two Square instances based on area.

        Parameters:
            other (Square): The other Square instance for comparison.

        Returns:
            bool: True if area is greater than or equal, False otherwise.
        """
        return self.area() >= other.area()

    def __lt__(self, other):
        """
        Less than comparator for two Square instances based on area.

        Parameters:
            other (Square): The other Square instance for comparison.

        Returns:
            bool: True if area is less, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Less than or equal to comparator for two Square instances based on area.

        Parameters:
            other (Square): The other Square instance for comparison.

        Returns:
            bool: True if area is less than or equal, False otherwise.
        """
        return self.area() <= other.area()

