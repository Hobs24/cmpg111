from calculator import square
import pytest
# using the pytest library to test the code to handle the running of test// download pytest via pip

def test_positive():
    assert square(2) == 4
    assert square(3) == 9
    assert square(5) == 25


def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9


def test_zero():
    assert square(0) == 0

#raises() function allow to express that you expect an exception to be raised
def test_str():
    with pytest.raises(TypeError):
        square("cat")
