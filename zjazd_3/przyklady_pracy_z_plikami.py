
#file = open("dane/przykladowy_exel.csv")  # otwieranie i zamykanie pliku , kiedys zawsze trzeba bylo plik zamyksac
#print(file.read())
#file.cose()

#with open("dane/przykladowy_exel.csv") as f:    # nowy sposób plik sam jest zamykany po wykonaniu polecenia
#    print(f)

with open('dane/nowy_pli.txt', 'w', encoding='utf-8') as f:   # tworzenie pliku
    f.write("Jakis tekst")

with open('dane/nowy_pli.txt', encoding='utf-8') as f:   # czytanie pliku
    print(f.read())

with open('dane/nowy_pli.txt', 'a', encoding='utf-8') as f:   # otworzenie z mozliwoscia dopisania
    f.write("Jakis tekst")

with open('dane/nowy_pli.txt', 'r', encoding='utf-8') as f:   # otworzenie bez mozliwosci dopisania
    f.write("Jakis tekst")

with open('dane/nowy_pli.txt') as f:
    for line in f:
        print(line.lower())