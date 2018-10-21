# napisz funkcje obliczjaca liczbe znakow w zadanym napisie pomiedzy zadanymi znakami
#znaki pomiedzy ktorymi odbywac sie zlicznaie, powiiiny byc argumentami z wartosci domysnymi - odpowiednio <i>.
# nawaisy moge byc zagniezdzone i moga wystapic wiele razy. Znaki pomiedzy zagniezdzonymi nawiasmi liczone sa zgodnie z poziomem zagniezdzenia

#ciag_znakow1 = ('ala ma <kota> a kot ma ale')
# 4
#ciag_znakow2 = ('ala [kota [a kot]] ma [ale]', '[', ']')
#18
#ciag_znakow3 = ('a <a<a<a>>>')
#6

def policz_znaki(napis, start ="<", end=">" ):
    wynik = 0
    start_i = 0
    end_i = 0
    if "<" in napis:
        start_i = napis.index('<')
    if ">" in napis:
        end_i = napis.index('>')
    if start_i and end_i:
        wynik = end_i - start_i
    return wynik


def test_policz_znak_pusty_napis():
    assert policz_znaki('') == 0

def test_policz_znaki_bez_znacznikow():
    assert policz_znaki('to jest napis') == 0

def test_policz_znaki_jeden_level_wartosci_domyslne():
    assert policz_znaki('ala ma <kota> a kot ma ale') == 4

def test_policz_znaki_jeden_dwa_level_wartosci_domyslne():
    assert policz_znaki('ala [kota [a kot]] ma [ale]', '[', ']') == 18

def test_policz_znaki_trzy_levele():
    assert policz_znaki('a <a<a<a>>>') == 6


