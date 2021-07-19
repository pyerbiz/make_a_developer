""" a module with multiple binary search object definitions"""


class binary_search_base:
    def __init__(self, array, value) -> None:
        self.array = array
        self.value = value

    def simple_binary_search(self):

        """ take a list and a value, search for the value in the list
        and return its index if found """

        first = 0
        last = len(self.array) - 1

        while last >= last:
            mid = (last + first) // 2
            fetched_val = self.array[mid]

            if fetched_val == self.value:
                return mid
            elif fetched_val > self.value:
                last = mid - 1
            else:
                first = mid + 1
        print(f"didn't find the given value")
        return None
