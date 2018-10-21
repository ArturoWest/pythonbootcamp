#cena_za_kg = 10.0
#waga = 2.5
#naleznosc = waga * cena_za_kg

#out = f"""Cena za kg: {cena_za_kg}
#Waga: {waga}
#Należność: {naleznosc}
#"""

#print(out)

def naleznosci(waga, cena):
 #   """
 #      Liczymy cene
 #       :param cena: cena za kilogram - numeric
 #       :param waga: liczba kg - numeric
 #       :return: naleznosc - numeric
 #   """
    return waga * cena

def rachunek(waga, cena):

    out = f"""cena za kg: {cena}
    waga: {waga}
    naleznosc: {naleznosci(waga, cena)}
    """
    print(out)

def test_naleznosci():
    assert naleznosci(10, 10) == 100
    assert naleznosc(0, 1) == 0


rachunek(10, 2.5)
