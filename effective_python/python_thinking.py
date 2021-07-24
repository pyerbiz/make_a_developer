""" module containing callables for explaining python concepts"""


class CharEncode:
    def __init__(self) -> None:
        pass

    def bytes_vs_string(self):
        a = b"h\x65llo"
        print(f"bytes to list {list(a)}")
        print(f"printed bytes data{a}")

    def to_str(self, bytes_or_string):
        if isinstance(bytes_or_string, bytes):
            value = bytes_or_string.decode("utf-8")
        else:
            value = bytes_or_string
        return value

    def to_bytes(self, bytes_or_string):
        if isinstance(bytes_or_string, str):
            value = bytes_or_string.encode("utf-8")
        else:
            value = bytes_or_string
        return value


class UnpackingSwap:
    """example unpacking to swap value without creating a temp var
    using bubble sort"""

    def bubble_sort_temp_var(a):
        for _ in range(len(a)):
            for i in range(1, len(a)):
                if a[i] < a[i - 1]:
                    temp = a[i]
                    a[i] = a[i - 1]
                    a[i - 1] = temp
        return a

    def bubble_sort(a):
        for _ in range(len(a)):
            for i in range(1, len(a)):
                if a[i] < a[i - 1]:
                    a[i - 1], a[i] = a[i], a[i - 1]
        return a
