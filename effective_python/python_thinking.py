""" module containing callables for explaining python concepts"""


class Items:
    def __init__(self) -> None:
        pass

    def bytes_vs_string(self):
        a = b"h\x65llo"
        print(f"bytes to list {list(a)}")
        print(f"printed bytes data{a}")
