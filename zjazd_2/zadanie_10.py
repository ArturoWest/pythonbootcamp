# napisz program zliczajacy liczbe wystapien kazdego znaku w podanym przez uzytkownika napisie

napis = input("podaj napis: ")
liczniki_liter = {}
# zliczyc
# rozwiazanie pierwsze przy pomocy petli for
#for litera in napis:
#    if litera in liczniki_liter:
#       liczniki_liter[litera] = liczniki_liter[litera] + 1
#    else:
#       liczniki_liter[litera] = 1

# rozwiaznie drugie przy pomocy GET
for litera in napis:
    liczniki_liter[litera] = liczniki_liter.get(litera, 0) +1
# wyswietlic

for litera in liczniki_liter:
    print(f'litera:  {litera} wystapila {liczniki_liter[litera]} razy')
