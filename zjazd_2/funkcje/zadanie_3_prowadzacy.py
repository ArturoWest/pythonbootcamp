def policz_znaki(napis, start ="<", end=">" ):
    poziom_zaglebienia = 0
    wynik = 0
    for znak in napis:
        if znak == "<":
            poziom_zaglebienia +=1
        if znak == ">":
            poziom_zaglebienia -=1

    return poziom_zaglebienia

def test_0_poziom_zaglebienia():
    assert policz_znaki('to jest napis') == 0

def test_1_poziom_zaglebienia():
    assert policz_znaki('to < jest napis') == 1

def test_2_poziom_zaglebienia():
    assert policz_znaki('to < jest < napis') == 2

def test_3_poziom_zaglebienia():
    assert policz_znaki('to < jest < na <pis') == 3

def test_2_poziom_zaglebienia():
    assert policz_znaki('to < jest < na < pis>') == 2
