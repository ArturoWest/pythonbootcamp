liczby = [5, 2, 1, 4, 3]

min_i = None
max_i = None

print(liczby)
indeksy = list(range(len(liczby)))


for i in liczby: # do czego mamy się odwoływać ?
    if min_i == None or liczby[i] < liczby[min_i]:
        min_i = i
    if max_i == None or liczby[i] > liczby[max_i]:
        max_i = i
    print(min_i)
    print(max_i)

if min_i is not None and max_i is not None:
    tmp = liczby[min_i]
    liczby[min_i] = liczby[max_i]
    liczby[max_i] = tmp





assert liczby == [1, 2, 5, 4, 3]
