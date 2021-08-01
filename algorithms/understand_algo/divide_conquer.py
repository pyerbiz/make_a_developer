""" the technique of D&C"""


class DivideConquer:
    def __init__(self) -> None:
        pass

    def recursive_addition(self, array):

        if array == []:
            return 0
        return array[0] + DivideConquer.recursive_addition(array)

    def recursive_length(self, array):

        if array == []:
            return 0
        return 1 + DivideConquer.recursive_length(array)

    def recursive_max(self, array):

        """ Assumption: At least 2 elements passed, no equal elements"""

        if len(array) == 2:
            return array[0] if array[0] > array[1] else array[1]
        current_max = DivideConquer.recursive_max(array[1:])
        return array[0] if array[0] > current_max else current_max
