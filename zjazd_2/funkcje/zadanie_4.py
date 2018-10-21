# zadanie numer 4
"""
Wersja 1.
Funkcja przyjmuje zmienna cena oraz nieokreslona liczbe tekstow.
W tych tekstach trzeba zmienic $cena na wartosc zmiennej cena
Zwroc zlaczony tekst - kazdy tekst w nowej linii

"""
def formatuj(cena, *args):
    out = []
    for text in args:
        text = text.replace("$cena", str(cena))
        out.append(text)
    return "\n".join(out)


def test_formatuj():
    assert formatuj(
        10,
        'koszt $cena PLN',
        'kwota $cena brutto'
    ) == "koszt 1- PLN\nkwota 10 brutto"

    assert formatuj(
        10,
        'koszt $cena PLN',
        'kwota $cena brutto',
        'sumarycznie $cena'
    ) == "koszt 1- PLN\nkwota 10 brutto\nsumarycznie 10"
