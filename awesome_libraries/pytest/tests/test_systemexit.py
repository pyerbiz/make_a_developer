import pytest


def f():
    raise SystemExit(1)


def g():
    f = {"A": "g"}
    return f["A"]  # raise Keyerror to pass


def test_mytest():
    with pytest.raises(SystemExit):
        f()


def test_keyerro():
    with pytest.raises(KeyError):
        g()
