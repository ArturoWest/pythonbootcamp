# napisz program zliczajacy liczbe znakow w podanym przez uzytkownika napisie nawiasami <>. Nawiasy moge wypstapic tylko raz
SAMOGLOSKI = "aeiou"
napis = input('podaj napis:' )

ile_samoglosek = 0

for znak in napis:
    # jesli samogloska to powieksz licznik
    if znak in SAMOGLOSKI:
        ile_samoglosek += 1
print(f"W teksicei : {napis}, znajduje sie {ile_samoglosek} samoglosek")


my_tekst = input('podaj tekst: ")'
# rozwiazanie z sali

nawias1 = 0
nawias2 = 0

for index, i in enumerate(my_tekst'):
    if i == "<":
        nawias1 = index
    if i ==">":
        nawias2 = index
print(nawias2 - nawias1 -1)

# rozwiazanie prowadzacy

czy_miedzy_namie = False
licznik = 0

for znak in my_text:
    if znak == "<":
        czy)miedzy_nawiasami = True
    elif znak ==">":
        czy_miedzy_nawiasami = False

    elif czy_miedzy_nawiasmi:
        licznik += 1
print(licznik)