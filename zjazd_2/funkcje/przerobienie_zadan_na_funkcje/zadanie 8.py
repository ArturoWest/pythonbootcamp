print("Podaj rok urodzenia")
print("________________________")
rok_urodzenia = int(input("Podaj rok urodz: "))

import datetime

now = datetime.datetime.now()
print("aktualny rok", now.year)
print("aktualny miesiąc", now.month)

wiek = 2018 - rok_urodzenia

if wiek >= 18:
    print("Jesteś pełnoletni")
else:
    print('Przykro mi nie możesz kupić alkocholu')
