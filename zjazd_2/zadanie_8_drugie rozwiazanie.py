produkty = {'pomidor':10, 'jablko':11, 'banan':4}

# wypisanie dostepnych produktow dla uzytkwoniak
while True:
    print("-"*40)
    print('Nasza zielnik oferuje: ')
    for produkt in produkty:
        print(f' - {produkty} - {produkty[produkt]} PLN')
    print()
    komenda = input("Co chcesz [k]upic, [koniec] by przerwac zakupy")
    if komenda == 'koniec':
        break
    produkt_wybrany = input('co chesz kupic?: ')

    if produkt_wybrany not in produkty:
        print("Nie mamy takiego produktu!")
        continue

    waga = float(input(f'ile chcesz kupic [{produkt_wybrany}]:'))

    cena = produkty[produkt_wybrany]

    koszt = waga * cena

print("-"*40)
print(f'za zakupy zaplacisz: {koszt}')