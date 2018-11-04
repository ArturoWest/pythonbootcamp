# napisz program wczytujacy plik z logami aktywnosci uzytkownikow w systemie. na podstawie wczytanych danych wyslwietl inforamcje o sumaryczym czasie przebywania kazdego uzytkownika w systemie.
# przyklad uzycia:
# $ python read_logppy logs.txt
# - user-1: 92 s
# - user-2: 51 s
# - user-3: 20 s

import sys

if len(sys.argv) > 1:
    file_name = sys.argv[1]
else:
    file_name = "dane/logs.txt"
user_last_login = {}
user_total_time = {}
with open(file_name) as f:
    for line in f:
        login, action, time = line.split(";") # przypisanie
        time = int(time)
    #print(login, action, time)
        if action == "LOGIN":
            user_last_login[login] = time
        if action == "LOGOUT":
            user_total_time[login] = user_total_time.get(login, 0) + time-user_last_login[login]

def sort_key(x):
    return x[1]

print('Czas przebywana w systemie')
#for login in user_total_time:
    #print(f' - {login}: {user_total_time[login]}')
for item in sorted(user_total_time.items(), key=sort_key, reverse=True):
#for item in sorted(user_total_time.items(), key=lambda x: x[1], reveres=True)
    print(item)






#def pobierz_dane():
#   """
#    Funkcja zwraca tuplę tupli zawierających dane pobrane z pliku csv
#    do zapisania w tabeli.
#    """
#    dane = []  # deklarujemy pustą listę
#    with open('dane/logs.txt', "r") as zawartosc:  # otwieramy plik do odczytu
#            for linia in zawartosc:
#                linia = linia.replace("\n", "")  # usuwamy znaki końca linii
#                linia = linia.replace("\r", "")  # usuwamy znaki końca linii
#                linia = linia.decode("utf-8")  # odczytujemy znaki jako utf-8
#                # dodajemy elementy do tupli a tuplę do listy
#                dane.append(tuple(linia.split(",")))


#    return tuple(dane)  # przekształcamy listę na tuplę i zwracamy ją

#print(pobierz_dane())