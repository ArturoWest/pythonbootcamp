#LICZBA_DNI_TYGODNIA = 7

#numer_dnia = 1
#suma_temperatur = 0

#nim_ = None
#max_ = None

#while numer_dnia <= LICZBA_DNI_TYGODNIA:
#    temp = int(input(f"Podaj temperaturę z dnia {numer_dnia}"))
#    suma_temperatur += temp
#    if numer_dnia == 1:
#        min_ = temp
#        max_ = temp
#    else:
#        if temp < min_:
#            min_ = temp
#        if temp > max_:
#            max_ = temp

#    numer_dnia += 1

#srednia_temperatur = suma_temperatur / LICZBA_DNI_TYGODNIA

#print(f' Srednia temperatura w tygodniu to {srednia_temperatur}')
#print (f'Temperatura minimlana to było: {min_}')
#print (f'Temperatura maksymalna to było: {max_}')


# 1 trzeba pobrać dane
LICZBA_DNI_TYGODNIA = 7

def pobieranie_danych(ile_razy = LICZBA_DNI_TYGODNIA):
    temperatury = []
    for i in range(ile_razy):
        temp = int(input(f"Podaj temperaturę z dnia {i+1}: "))
        temperatury.append(temp)
    return temperatury

# 2 trzeba ustalic srednia
def srednia_temp(temperatury):
    srednia_temperatura = sum(temperatury) / len(temperatury)
    return srednia_temperatura
# 3 trzeba policzyc minmax
def znajdz_ekstrema(temperatury):
    min_ = min(temperatury)
    max_ = max(temperatury)
    return min_, max_
# 4 prezentuj dane
def prezentuj_dane(srednia_temperatura, min_, max_):
    print(f'Srednia temperatura w tygodniu to {srednia_temperatura}')
    print(f'Temperatura minimlana to było: {min_}')
    print(f'Temperatura maksymalna to było: {max_}')

def main():
    dane = pobieranie_danych()
    sr_temp = srednia_temp(dane)
    min_, max_ = znajdz_ekstrema(dane)
    prezentuj_dane(sr_temp, min_, max_)

main()