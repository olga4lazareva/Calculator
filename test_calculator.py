from core.calculator import calculate

def test_add():
    assert calculate("add", 2, 3) == 5

def test_divide():
    assert calculate("divide", 10, 2) == 5
