Liczba = float(input("Podaj liczbę: "))

print("Wynik ", Liczba % 2 == 0 and Liczba % 3 == 0 and (Liczba > 10 or Liczba == 7))

liczba = float(input("Podaj liczbę: "))

podzielna_przez_2 = liczba % 2 == 0
podzielna_przez_3 = liczba % 3 == 0
wieksza_niz_10 = liczba > 10
rowna_7 = liczba == 7

print(podzielna_przez_2, podzielna_przez_3, wieksza_niz_10, rowna_7)

wynik = (podzielna_przez_2 and podzielna_przez_3 and wieksza_niz_10 or rowna_7)

print(wynik)
