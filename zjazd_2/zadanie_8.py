# Napisz program wyliczajacy kwote nalezna za zakupiony towar na podstawie podanej przez uzytkownika wagi i nazwy produktu
#Do przechowywania informacji o cenie za kilogram danego produktu uzyj slownika. Wypisz wszystkei dostepne produkty w sklepie.

# opis dostepnych produktow
produkty = {'pomidor':10, 'jablko':11, 'banan':4}

# wypisanie dostepnych produktow dla uzytkwoniak
print('Nasza zielnik oferuje: ')
for produkt in produkty.items():
    name, cena = produkt
    print(f' - {name} - {cena} PLN')

produkt_wybrany = input('co chesz kupic?: ")')
waga = float(input(f'ile chcesz kupic [{produkt_wybrany}]:'))

cena = produkty[produkt_wybrany]

koszt = waga * cena

print(f'wyliczony koszt to: {koszt}')