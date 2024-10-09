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

def test_mul():
    assert mul(1,2) == 2
    assert mul(-1,2) == -2
    assert mul(-1,-2) == 2
    assert mul(0,0) == 0
    assert mul(0,34) == 0

def test_div():
    assert div(1,2) == 0.5
    assert div(-1,2) == -0.5
    assert div(-1,-2) == 0.5
    assert div(0,1) == 0
    assert div(5,0) == "Nullaval nem lehet osztani"