#miasto_a = input("Podaj nazwę miasta A: ")
#miasto_b = input("Podaj nazwę miasta B: ")

#dystans = float(input(f"Podaj dystans między {miasto_a}-{miasto_b}"))
#cena_paliwa = float(input("Jaka jest cena paliwa: "))
#spalanie = float(input("Określ spalania na 100km: "))

#koszt = ((dystans / 100) * spalanie * cena_paliwa)

#output = f"""
#Miasto A: {miasto_a}
#Miasto B: {miasto_b}
#Dystans {miasto_a}-{miasto_b}: {dystans}
#Cena paliwa: {cena_paliwa}
#Spalanie na 100km: {spalanie}

#Koszt przejazdu {miasto_a}-{miasto_b} to {koszt} PLN"""

#print(output)


# pobieranie danych

def pobieranie_danych():
    miasto_a = input("Podaj nazwę miasta A: ")
    miasto_b = input("Podaj nazwę miasta B: ")
    dystans = float(input(f"Podaj dystans między {miasto_a}-{miasto_b}"))
    cena_paliwa = float(input("Jaka jest cena paliwa: "))
    spalanie = float(input("Określ spalania na 100km: "))
    return miasto_a, miasto_b, dystans, cena_paliwa, spalanie

# oblicznie kosztu

def obliczanie_kosztu(miasto_a, miasto_b, dystans, cena_paliwa, spalanie):
    koszt = int((dystans / 100) * spalanie * cena_paliwa)
    return koszt

    dane = pobieranie_danych()

    print(dane)
    print(type(dane))

    koszt = obliczanie_kosztu(*dane) # zapis obliczanie_kosztu(*dane) oznacza obliczanie_kosztu(dane[0], dane[1], dane[2], dane[4])

    print(koszt)

def drukuj_wynik(miasto_a, miasto_b,dystans, cena_paliwa, spalanie):
    koszt = obliczanie_kosztu(miasto_a, miasto_b, dystans, cena_paliwa, spalanie)
    out = f"""
    Miasto A: {miasto_a}
    Miasto B: {miasto_b}
    Dystans {miasto_a}-{miasto_b}: {dystans}
    Cena paliwa: {cena_paliwa}
    Spalanie na 100km: {spalanie}
    Koszt przejazdu a-b to: {koszt}"""
    return out

# prezentowanie danych

dane = pobieranie_danych()
print(drukuj_wynik(*dane))