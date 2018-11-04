x =1
napis = "To jest napis"
slownik = {}

def foo():
    pass

print(type(x), type(napis), type(slownik),type(foo))

# definicja klasy
class Animal:

    licznik = 0
    gatunek = "Canis Lupus"

    def __init_(self, gatunek): # inicjalizujemy nowy obietk nowa instance (pierwszy argument wskazuje na instancje)
        self.gatunek = gatunek  # self wskazuje na konkretna instancje - atrybut instancji, obiektu
        self.licznik = 0
    def __str__(self):
        return "Animal"




#tworzenie instancji danej klasy
azor = Animal("Canis Familiaris")
rudolf = Animal("Rangifer tarandus")

print(azor) # reprezantacja napisowa instancji mojej klasy
print(type(azor))
print(dir(azor))
print(azor.gatunek) # wypisanie atrybutu
print(rudolf)