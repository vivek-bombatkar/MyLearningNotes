import pytest

def my_fun(s: str = None):
    try:
        return str*2
    except TypeError:
        return None

def test_my_fun():
    assert my_fun('ABC') == None