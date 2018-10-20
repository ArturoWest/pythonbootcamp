my_dict = {
	"pierwsza": "a",
	"druga": "b"
}

my_dict['trzecia'] = 'c'

d2 = dict()
d2 = dict([('a',1), ('b',2)])

print('d2: ', d2)

print(my_dict['pierwsza'])

#print(my_dict['a'])

print(my_dict['druga'])

print(my_dict.items()) # drukuje pary

print(my_dict.keys())

print(my_dict.values())

produkt1 = {'nazwa': 'Koper', 'cena': 3}

produkt2 = {"nazwa": "Kasza", "cena": 1.99}

produkty = [produkt1, produkt2]

print("Produkty w lodowce: ")
for p in produkty:
    print(p['nazwa'])

for k in produkt1:
    print(k, produkt1[k])

print()
a = {"a":1, "b":2}
b = {"c":3, "d":4}

print(dir(a))
print()
a.update(b)
print(a)