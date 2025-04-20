from src.math_operations import add, sub 

def test_add():
    """Test the add function."""
    assert add(1, 2) == 3, "Should be 3"
    assert add(-1, 1) == 0, "Should be 0"
    assert add(-1, -1) == -2, "Should be -2"

def test_sub():
    """Test the sub function."""
    assert sub(2, 1) == 1, "Should be 1"
    assert sub(1, 1) == 0, "Should be 0"
    assert sub(-1, -1) == 0, "Should be 0"