""" recursion and definition of stack"""


class Recursion:
    def __init__(self) -> None:
        pass

    def factorial(x):
        if x == 1:
            return 1
        else:
            return x * Recursion.factorial(x - 1)
