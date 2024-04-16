import pytest

def sum (a, b):
 return a + b
def test_assert_sum():
    assert sum(1,2) == 3
def sub (a, b):
 return a - b
def test_assert_sub1():
    assert sub(1,2) == -1
def test_assert_sub2():
    assert sub(3,2) == 1
def mult (a, b):
 return a*b
def test_assert_mult1():
    assert mult(1,2) == 2
def test_assert_mult1():
    assert mult(5,8) == 40

def div (a, b):
 return a/b


def test_assert_div1():
    assert div(1,2) == 0.5

def test_assert_div2():
    assert div(40,5) == 8

def test_asert_div3():
    with pytest.raises(ZeroDivisionError):
        assert div(1, 0)
