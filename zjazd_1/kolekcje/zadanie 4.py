
# 1 stworzyc liste od 0 do 100
lista = list(range(101))
# 2 utworzyc liste podzielnych przez 3 lub 5
wynik = []

# 3 przejsc przez liste z 1. i pododawac do list z kroku 2
for el in lista:
    if el % 3 == 0 or el % 5 == 0:
        wynik.append(el)
# 4 wypisac
print('Liczby podzielne przez 3 lub 5:')
print()
for el in wynik:
    print(el)
    
print()
print(f'w przedziale 0-100 jest {len(wynik)} liczb podzielnych przez 3 lub 5')