
#def przywitaj_sie(): # funkcja ktora nic nie robi
#    return 1

#przywitaj_sie()

#print(type(przywitaj_sie()))
#print(przywitaj_sie())

#y = przywitaj_sie()
#print(type(y))
#print(y)

def say_hello(imie, wiek, wzrost, waga):
    if wzrost > 178:
        print("ale z ciebie dragal")
    if waga > 100:
        print("boczek")
    if wiek > 38:
        print ("ale jestes stary")

lista_osob = [
{       'imie': 'Rafał',
        'wiek': 80,
        'wzrost': 188,
        'waga': 100,},
{   'imie': 'Jacek',
        'wiek': 33,
        'wzrost': 189,
        'waga': 90,}
            ]

for osoba in lista_osob:
    say_hello(osoba['imie'], osoba['wiek'], osoba['wzrost'], osoba['waga'])
