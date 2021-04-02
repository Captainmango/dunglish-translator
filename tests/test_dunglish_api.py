from dunglish_api import api, translator


def test_adder():
    assert api.test.adder(3,2) == 5

def test_minus():
    assert api.test.minus(3,3) == 0

def test_speaks():
    assert translator.translator.speak() == print("this worked")