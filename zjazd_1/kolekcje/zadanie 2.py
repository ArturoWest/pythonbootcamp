# zebranie liczb nie więcej niź 10
n = int(input("Podaj liczbę wprowadzanych liczb n: "))
numer_liczby = 1

while True:
    dane_wejsciowe = input("Podaj liczbę: ")

    liczba = int(dane_wejsciowe)

    if numer_liczby == n:
        break
    numer_liczby += 1

print(dane_wejsciowe)