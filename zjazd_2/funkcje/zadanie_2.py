# napisz funkcje zwracajaca zbior wszystkich znakow wystepujacych w napisie wiecej niz zadana liczba razy
# 1 policzyc wystapienia ze {'a':3, 'b':2, 'c':5}
# 2 sprawdzic ktore liczniki sa wieksze niz prog i dodac do zbioru wyjsciowego x]'x'] >2
# 3 zwrocic


def wiecej_niz(napis, prog):
    licznik_liter = {}
    wynik = set()
    #zliczyć
    for litera in napis:
        litera = litera.lower()
        licznik_litera[litera] = licznik_liter.get(litera, 0) + 1

    for key, value in licznik_liter.items():
        if value > prog:
        wynik.add(key)
    return wynik

def test_wiecej_niz_dla_niepustego_napisu():
    assert wiecej_niz('aaaaa', 10) == set()

def test_wiecej_niz_dla_pustego_napisu():
    assert wiecej_niz("",0) == set() #set() to pusty zbior

def test_wiecej_niz_dla_niepustego_napisu():
    assert wiecej_niz('aaaaabbbccd', 2) == {'a', 'b'} # a i b dlatego ze wystepuja w ciagu wiecej niz 2 razy a tego sie wymaga (druga zmienna w nawiasie)