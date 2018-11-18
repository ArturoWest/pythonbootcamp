
import sys
print(sys.path)


from ..zjazd_3.zadanie8.py import Vector, Foo, dict as pisany_slownik 
#from zadanie8 import Vector, Foo, dict as pisany_slownik


v1 = Vector(1, 2)
v2 = Vector(1, 2)
print(v1+v2)

x = Foo()

pusty_slownik = pisany_slownik(1, 2)
print(type(pusty_slownik))

