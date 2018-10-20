# napisz program zliczajacy liczbe unikalnych liczb wprowadzonych przez uzytkownika. Sprawdz jak dluzo z tych liczb jest liczbami parzystymi w zakresie 0-100 - w tym celu skorzystaj z operatora iloczynu

# liczby przekazane przez uzytkownia

liczby = set()

while True:
    komenda = (input("Podaj liczbę, lub wpisz k by zakończyć: "))

    if komenda == 'k':
        break
    liczba = int(komenda)
    liczby.add(liczba)

print(liczby & set(range(2,101, 2)))
print(len(liczby & set(range(2,101, 2))))
