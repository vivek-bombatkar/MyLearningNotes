from unittest.mock import patch

def my_upper_function():
    return None

def my_func():
    try:
        return my_upper_function().upper()
    except TypeError:
        return None

def test_my_func():
    with patch('unittest_patch.my_upper_function') as upper_function:
        upper_function.return_value = "dada"
        assert my_func() == "DADA"
