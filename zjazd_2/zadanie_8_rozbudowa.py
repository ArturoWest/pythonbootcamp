produkty = {'pomidor': 10, 'jablko': 11, 'banan': 4}
magazyn = {'pomidor': 15, 'jablko': 20, 'banan': 40}

do_zaplaty = 0
# wypisanie dostepnych produktow dla uzytkwoniak
while True:
    print("-" * 40)
    print('Nasza zielnik oferuje: ')
    for produkt in produkty:
        print(f' - {produkt} - {produkty[produkt]} PLN')

    komenda = input("Co chcesz zrobic: [k]upic, [d]odać, [koniec] by przerwac zakupy: ")
    if komenda == 'koniec':
        break
    produkt_wybrany = input('co chesz kupic?: ')

    if produkt_wybrany not in produkty:
        print("Nie mamy takiego produktu!")
        continue

    waga = float(input(f'ile chcesz kupic [{produkt_wybrany}]: '))
    if magazyn[produkty_wybrany] < waga:
        print(f'Mamy za mało {produkt_wybrany}, pozostalo {magazyn[produkt_wybrany]} kg')
        continue
    magazyn[produkt_wybrany] = magazyn[produkt_wybrany] - waga
    cena = produkty[produkt_wybrany]
    koszt = waga * cena
    do_zaplaty += koszt


print("-" * 40)
print(f'za zakupy zaplacisz: {do_zaplaty}')