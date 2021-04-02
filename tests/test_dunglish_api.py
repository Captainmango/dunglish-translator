from dunglish_api.api import test


def test_adder():
    assert test.adder(3,2) == 5

def test_minus():
    assert test.minus(3,3) == 0