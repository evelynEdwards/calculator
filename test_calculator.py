from calculator import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5

def test_divide():
    assert divide(6, 2) == 3

def test_subtract():
    assert subtract (3, 2) == 1

def test_multiply():
    assert multiply (6, 2) == 12

def test_circleArea():
    assert CircleArea(-4) == "Error"

def test_multiply_zero():
    # Arrange
    a, b = 7, 0
    # Act
    result = multiply(a, b)
    # Assert
    assert result == 0
