# w sesji interaktywnego srodowiska stworz nastepujace struktuy danych korzystajac ze skroconej wersji zapisu:
# liste zawieraca liczby zmiennoprzecinkowe od 0.0 do 1.0 z krokiem 0.1
# zbior tupli
# nie nadążam na tym zadaniu ;(

kwadraty1 = [(x, x**2) for x in range(1, 101)]
print(kwadraty1)
print([i/10 for i in range(101)])
print()
kwadraty2 = {(x, x**2) for x in range(1, 101)}
print(kwadraty2)
print([i/10 for i in range(101)])
print()
#kwadraty3 = {(x: x**2) for x in range(1, 101)} # nie działa - nie wiem co miał prowadzący na myśli
#print(kwadraty3)
#print([i/10 for i in range(101)])


kwadraty = {(x, x**2, x**3) for x in range(1, 101)}


zbior_napisow = {'abc', 'ala ma kota', 'slowacki wielkim poeta byl', 'super'}
print({x:len(x) for x in zbior_napisow})