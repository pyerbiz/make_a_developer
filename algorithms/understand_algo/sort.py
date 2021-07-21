""" a module with multiple sorting methods"""


class SortBase:
    def __init__(self, arr) -> None:
        self.arr = arr

    def selection_sort(self):
        """ self contained array sort"""
        _arr = self.arr.copy()
        for i in range(len(_arr)):
            min = i
            for j in range(i + 1, len(_arr)):
                if _arr[j] < _arr[min]:
                    min = j
            _arr[min], _arr[i] = _arr[i], _arr[min]

        return _arr

    def _find_smallest_in_array(self):
        smallest = self.arr[0]
        smallest_index = 0
        for i in range(1, len(self.arr)):
            if self.arr[i] < smallest:
                smallest = self.arr[i]
                smallest_index = i
        return smallest_index

    def selection_sort_alt(self):
        sorted_arr = []
        for i in range(len(self.arr)):
            smallest_index = sort._find_smallest_in_array(self.arr)
            sorted_arr.append(self.arr.pop(smallest_index))
        return sorted_arr
