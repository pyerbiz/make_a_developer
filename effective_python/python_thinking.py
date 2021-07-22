""" module containing callables for explaining python concepts"""


class Items:
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
