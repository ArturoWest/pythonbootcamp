# napisz program ktory posortuje liczby w tablicy przy wykorzystaniu algotytmu 'sortowanie przez wzbieranie

liczby = [5,2,1,4,3]

print('Przed: ', liczby)

for i in range(len(liczby)): # range ponieważ chcemy brać indeksy tych liczb
    index_minimum = i
    print('i:', i, 'liczby: ', liczby[i:])
    for j in range(i+1, len(liczby)): # i+1 bo w każdym kroku zaczynamy od następnej liczby pętle i sprawdzamy z następnymi liczbami czy jest mniejsza
        if liczby[j] < liczby[index_minimum]:
            index_minimum = j
    liczby[i], liczby[index_minimum] = liczby[index_minimum], liczby[i]
    print('i: ', i, 'liczby:', liczby)
print("Po: ", liczby)

# pętla z google skopiowana
#def Insert_sort(A):
#    for i in range(1,len(A)):
#        klucz = A[i]
#        j = i - 1
#        while j>=0 and A[j]>klucz:
#            A[j + 1] = A[j]
#            j = j - 1
 #       A[j + 1] = klucz