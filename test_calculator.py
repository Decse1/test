import pytest
from calculator import sum, sub, mul, div

def test_sum():
    assert sum(1,2) == 3
    assert sum(-1,2) == 1
    assert sum(-1,-2) == -3
    assert sum(0,0) == 0
    
def test_sub():
    assert sub(1,2) == -1
    assert sub(-1,2) == -3
    assert sub(-1,-2) == 1
    assert sub(0,0) == 0