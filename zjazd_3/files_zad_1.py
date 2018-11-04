
# napisz program wypisujacy na konsole zawartosc pliku wraz z numaerami linii . blsuz sytuacje gdy uzytkownik nie poda nazwy pliku lub poda bladna nazwe

#przyklady uzycia:
# $ pythoon test.txt
# 1: pierwsza linikja pliku
# 2: druga linia pliku

import sys
if len(sys.argv) > 1:
    nazwa_pliku = sys.argv[1]

    with open(nazwa_pliku) as f:
    #   i = 1
    #   for line in f:
    #        print(i, line, end="")
    #        i += 1
        for i, line in enumerate(f, start=1):
            print(i, line, end="")
else:
    print("Podaj nazwę pliku: ")

#with open('dane/test.txt', 'w', encoding='utf-8') as f:   # tworzenie pliku
#    f.write(f"1: pierwsza linia tekstu \n2: druga linia tekstu")

