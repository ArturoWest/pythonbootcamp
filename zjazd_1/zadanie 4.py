Miasto_A = input("Podaj Miasto A: ")
Miasto_B = input("Podaj Miasto B: ")

Cena_paliwa = int(input("Podaj cenę paliwa: "))

Spalanie_na_100km = int(input("Podaj spalanie na 100 km: "))

Dystans = int(input("Podaj odległość pomiędzy miastami: "))

koszt_przejazdu = (Cena_paliwa * Spalanie_na_100km * (Dystans / 100))

print("cena za paliwo", Cena_paliwa, 'średnie spalanie na 100 kilometrów', Spalanie_na_100km)

print(f'{koszt_przejazdu}')