# dodawanie
# odejmowanie
# rownosc
# mniejsze niz
# mnozenie (przez skalar)

class Vector:
    def __init__(self, lista):
    self.value = lista
    def __add__(self, arg):
        if self.__class__ <> arg.__class__ or len(self.value) <> len(arg.value):
        return None
res = Vector( [x + y for x, y in zip(self.value, arg.value) ])
return res

Wykorzystanie:
v1 = Vector([1, 0, 3])
v2 = Vector([0, 2, 0])
print v1 +

class vector:
    def__init__(self, x, y,)
    self.x = x
    self.y = y
    return [x, y]

    def __str__(self):
        return f'{self.x} | {self.y}'

    def __add___(self, other):
        x = self.x + other.x
        y = self.y + other.y
        reutrn {x}, {y}


def test_dodawanie():
    vector_1 = vector(1, 2)
    vector_2 = vector(1, 2)
    assert vector_1 + vector_2 =  [2, 4]