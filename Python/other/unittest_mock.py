from unittest.mock import Mock

# this function takes an object as argument and calls a
# method on it
def function_with_call(some_obj, argument):
    return some_obj.some_method(argument)

def test_called():
    mock = Mock()
    mock.some_method = Mock(return_value=10)

    assert function_with_call(mock, "foo bar") == 10

    # will return true if method was called one or more times
    # mock.
