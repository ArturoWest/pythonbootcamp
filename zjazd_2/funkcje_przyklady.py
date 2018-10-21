
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





def podzielna_przez_2(x):
    return x%2 == 0

def podzielna_przez_3(x):
    return x % 3 == 0  # takie wyrazenie zwraca zawsze True or False

print(podzielna_przez_2(12))
print(podzielna_przez_2(11))

#y = lambda x: x%2 == 0
#y = podzielna_przez_2
#print(y(4))
#print(y(5))


def wybierz(dane, warunek):
    """
    :param dane: lista liczb
    :param warunek: jakas funkcja sprawdzajca cos
    :return:  przeffiltrowna lista
    """
    out = []
    for element in dane:
        if warunek(elemet): # warnkiem czy podzielna przez 2
            out.append(element)
    return(out)
lista = [1,2,3,4,5,65,67,7,33,44,55,123]
print(wybierz(lista, podzielna_przez_2)) # podzielna przez 2 nie jest wywolywana jako funkcja tyklo akgument
print(wybierz(lista, lambda x: x % 3 == 0))
print(wybierz(lista, podzielna_przez_3))
