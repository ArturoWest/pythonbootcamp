print("Podaj wymiary opakowania w cm")
print("________________________")
wysokosc = float(input("Podaj wysokość opakowania: "))
szerokosc = float(input("Podaj szerokość opakowania: "))
dlugosc = float(input("Podaj długość opakowania: "))

obj = wysokosc * szerokosc * dlugosc

print('objętość opakowania jest większa od 1000cm3', obj > 1000)

print("________________")

if obj > 1000:
    print('objętość opakowania jest większa od 1000cm3')
else:
    print('objętość opakowania jest mniejsza lub równa 1000cm3')
