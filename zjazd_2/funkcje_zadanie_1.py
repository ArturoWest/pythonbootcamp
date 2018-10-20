# napisz funkcje sprawdzajaca, czy dane liczba jest liczba pierwsza

import pytest
def czy_wieksza_niz_3(liczba):
    if liczba>3:
        return True
    return False
def test_wieksza_niz_3_dla_wiekszej_niz_3():
    assert True == czy_wieksza_niz_3(4)