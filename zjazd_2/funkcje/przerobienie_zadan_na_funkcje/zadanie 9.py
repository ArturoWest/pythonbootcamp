#print("Podaj liczby oraz typ operacji jaki na nich zastosowac")
#print("________________________")
#pierwsza_liczba = int(input("podaj pierwszą liczbę: "))
#druga_liczba = int(input("podaj drugą liczbę: "))

#rodzaj_operacji = input("Podaj rodzaj operacji: ")

#if rodzaj_operacji == "+":
#    print('suma liczb', pierwsza_liczba + druga_liczba)
#if rodzaj_operacji == "-":
#    print('różnica liczb', pierwsza_liczba - druga_liczba)
#if rodzaj_operacji == "*":
#    print('iloczyn liczb', pierwsza_liczba * druga_liczba)
#if rodzaj_operacji == "/":
#    if druga_liczba ==0:
#        raise ValueError("Liczba druga powinna być dla tej operacji rózna od zera")
#    print('iloraz liczb', pierwsza_liczba / druga_liczba)
#else:
#   #print("Wybrałeś niezrozumiałą operację")
#    raise ValueError("Nieprawidłowa wartość dla parametru typu operacja")
#print ("Druga metoda")

#if rodzaj_operacji == "+":
#    print('suma liczb', pierwsza_liczba + druga_liczba)
#elif rodzaj_operacji =="-":
#    print('różnica liczb', pierwsza_liczba - druga_liczba)
#elif rodzaj_operacji =="*":
#    print('iloczyn liczb', pierwsza_liczba * druga_liczba)
#elif rodzaj_operacji =="/":
#    if druga_liczba ==0:
#        raise ValueError("Liczba druga powinna być dla tej operacji rózna od zera")
#        print('iloraz liczb', pierwsza_liczba / druga_liczba)
#else:
#    #print("Wybrałeś niezrozumiałą operację")
#    raise ValueError("Nieprawidłowa wartość dla parametru typu operacja")

# pobieranie liczb i wybór operacji

def pobieranie_dancyh():
    pierwsza_liczba = int(input("podaj pierwszą liczbę: "))
    druga_liczba = int(input("podaj drugą liczbę: "))

    rodzaj_operacji = input("Podaj rodzaj operacji: ")
    return pierwsza_liczba, druga_liczba, rodzaj_operacji

def kalkulator(pierwsza_liczba, druga_liczba, rodzaj_operacji):
    wynik = ""
    if rodzaj_operacji == "+":
        print('suma liczb', pierwsza_liczba + druga_liczba)
    if rodzaj_operacji == "-":
        print('różnica liczb', pierwsza_liczba - druga_liczba)
    if rodzaj_operacji == "*":
        print('iloczyn liczb', pierwsza_liczba * druga_liczba)
    if rodzaj_operacji == "/":
        if druga_liczba ==0:
            raise ValueError("Liczba druga powinna być dla tej operacji rózna od zera")
            print('iloraz liczb', pierwsza_liczba / druga_liczba)
    else:
         #print("Wybrałeś niezrozumiałą operację")
        raise ValueError("Nieprawidłowa wartość dla parametru typu operacja")

kalkulator(*pobieranie_dancyh)
