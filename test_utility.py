from utility import square
from utility import hello
import pytest


def test_default_hello():
    assert hello() == 'Hello, World'


def test_argument_hello():
    assert hello('Lee') == 'Hello, Lee'


def test_positive_square():
    assert square(2) == 4
    assert square(3) == 9


def test_negative_square():
    assert square(-2) == 4
    assert square(-3) == 9  


def test_zero_square():
    assert square(0) == 0


def test_string_square():
    with pytest.raises(TypeError):
        square('Lee')
    
