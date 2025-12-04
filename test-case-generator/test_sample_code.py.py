import pytest

def test_divide():
    assert divide(10, 2) == 5
    assert divide(10, -2) == -5
    assert divide(-10, 2) == -5
    assert divide(-10, -2) == 5
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

def test_is_valid_age():
    assert is_valid_age(18) is True
    assert is_valid_age(20) is True
    assert is_valid_age(17) is False

def test_greet():
    assert greet("Alice") == "Hello Alice"
    with pytest.raises(ValueError):
        greet("")
    with pytest.raises(ValueError):
        greet(None)