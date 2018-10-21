print("obliczanie sredniej temperatury z ostatnich dni")
print("________________________")

print("podaj liczbę dni n: ")
p = int(input("podaj temperaturę z poniedziałku: "))
w = int(input("podaj temperaturę z wtorku: "))
s = int(input("podaj temperaturę z środy: "))
cz = int(input("podaj temperaturę z czwartku: "))
pi = int(input("podaj temperaturę z piątku: "))
sob = int(input("podaj temperaturę z soboty: "))
n = int(input("podaj temperaturę z niedzieli: "))


temp = p + w + s + cz + pi + sob + n

print ("średnia temperatura tygodnia, {temp} / 7")
