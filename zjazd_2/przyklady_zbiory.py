zbior = {1,2,3,4} # nie ma wartosci jak w slownikach i sa to unikalne wartosci

print(zbior)

zbior.add(1)

print(zbior)

zbior.add("a")

print(zbior)

for i in zbior:
    print(i)

a = {1,2,3}
b = {3,4,5}

print(a | b)  # suma "|" - to jest symbol dodawania w zbiorach
print(a.union(b))
print(a - b)  # suma "-" - to jest symbol odejmowania w zbiorach
print(a.difference(b))
print(a & b)  # suma "&" - to jest czesc wspolna w zbiorach
print(a.intersection(b))
print(a ^ b)  # suma "&" - to jest roznica w zbiorach
print(a.symmetric_difference(b))

print(dir(a))

print(set(range(1,20)))

kwadraty = [x**2 for x in range(1, 101)]
print(kwadraty)
#alternatywa
kwadraty_alternatywa = []
for x in range(1, 101):
    kwadraty_alternatywa.append(x**2)
print(kwadraty_alternatywa)