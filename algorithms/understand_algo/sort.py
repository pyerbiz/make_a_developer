""" a module with multiple sorting methods"""


class sort:
    def __init__(self, arr) -> None:
        self.arr = arr

    def selection_sort(self):
        """"""
        _arr = self.arr.copy()
        for i in range(len(_arr)):
            min = i
            for j in range(i + 1, len(_arr)):
                if _arr[j] < _arr[min]:
                    min = j
            _arr[min], _arr[i] = _arr[i], _arr[min]

        return _arr
