def drukuj_linie():
    print('---'*40)

def zwroc_wartosc_wpisana():
    wartosc = input('podaj wartosc')
    return wartosc

drukuj_linie()

x = zwroc_wartosc_wpisana()
print(x)

a = [1,2,3,4,5]

def zwroc_sume_zdefiniowanej_listy():
    b = 1
    print(zwroc_sume_zdefiniowanej_listy())
    print(a)
    return sum(a)
print(zwroc_sume_zdefiniowanej_listy())
#def sumator(a):
#    return sum(a)

#x= [1,2,3,4,5]

#print(sumator(x))

def kalkulator(a, b, operacja = '+', opis = ""):
    if opis:
        print(opis)
    if operacja == "+":
        return a+b
    elif operacja == "-":
        return a-b
print(kalkulator(1, 2, opis = "dodawanie dwoch liczb"))
print(kalkulator(1, 2, "-"))
print(kalkulaotr(1, 2, "-", opis = 'odejmowanie dwoch liczb'))