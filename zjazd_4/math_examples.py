import math
print(math.sin(math.pi/2))

print(dir(math))


"""
Stwórz klasę sfera

s = Sfera(10)
s.promien # 10
s.objetosc() # 4188.78...
s.pole_powierzchni() # 1256.63...
"""

class Kula:
    def __init__(self, r):
        self.promien = r

    def objetosc(self):
        return (4/3) * math.pi * math.pow(self.promien, 3)

    def pole_powierzchni(self):
        return 4 * math.pi * self.promien ** 2

s = Kula(10)

print(s.objetosc())
print(s.pole_powierzchni())
