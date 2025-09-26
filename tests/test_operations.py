import pytest
from calculator.operations import add, subtract, multiply, divide, operate

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 3) == 2

def test_multiply():
    assert multiply(4, 3) == 12

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

def test_operate_add():
    assert operate('+', 2, 3) == 5

def test_operate_subtract():
    assert operate('-', 5, 3) == 2

def test_operate_multiply():
    assert operate('*', 2, 3) == 6

def test_operate_divide():
    assert operate('/', 10, 2) == 5

def test_operate_unknown_operator():
    with pytest.raises(ValueError):
        operate('^', 1, 2)
