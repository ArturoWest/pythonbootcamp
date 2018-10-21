# sposób 1
#Imię = "Jan"
#Wzrost = 180
#output1 = f"Imię: {Imię}\nWzrost: {Wzrost}"
#print(output1)

#sposob 2
#Imię = "Jan"
#Wzrost = 180
#output2 = f"""Opis faceta:
#    Imię: {Imię}
#    Wzrost: {Wzrost}
#"""

#print(output2)

def prezentu_osobe(imie, wzrost):
    wynik= f"""Opis faceta:
    Imię: {Imię}
    Wzrost: {Wzrost}
"""
    return wynik

def test_prezentuj_osobe():
    assert test_prezentuj_osobe("Rafał, 181") == """Opis faceta:
    Imię: Rafał
    Wzrost: 181"""