#liczby = input('Podaj liczny rozzilajaac je przecinkami:\n')
#liczby = liczby.split(",")
#print(liczby)
#i = 0
#while i < len(liczby):
#    suma = suma + int(liczby[i])
#    i += 1

#    print('suma', suma)
#    print('dlugosc', len(liczby))
#    print(suma / len(liczby))

liczby = []

while len(liczby) < 10:
    nowa_liczba = int(input("proszę podać liczbę: "))
    liczby.append(nowa_liczba)

#oblicznaia sredniej
srednia = sum(liczby)/len(liczby)
# wypisanie wyniku
print(srednia)

#liczby = []

#while len(liczby) < 10:
#    dane = int(input("proszę podać liczbę, lub [k] aby zakonczyc : "))
#    if dane
#    liczby.append(nowa_liczba)

# oblicznaia sredniej
#srednia = sum(liczby) / len(liczby)
# wypisanie wyniku
#print(srednia)