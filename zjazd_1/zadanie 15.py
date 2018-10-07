import random

# wylosuj położenie skarbu s_x; s_y
s_x = random.randint(1, 10)
s_y = random.randint(1, 10)
# wylosuj położenie gracza g_x, g_y
g_x = random.randint(1, 10)
g_y = random.randint(1, 10)
# oblicz minimlaną liczbę kroków między graczem a skarbem
min_krokow_po_wylosowaniu = abs(s_x - g_x) + abs(s_y - g_y)
# zapisz w zmiennej
# ustaw początkową liczbę ruchów na 0
# mechanika
while True:
    #   obliczanie minimalnej liczby kroków porzed ruchem
    min_l_ruchu_przed = abs(s_x - g_x) + abs(s_y - g_y)
    ruch = input("Wkonaj ruch [awsd]: ")
    ruch = ruch.lower()
    # poruszanie się gracza po planszy
    if ruch == "w":
        g_y += 1
    if ruch == "a":
        g_x -= 1
    if ruch == "s":
        g_y -= 1
    if ruch == "d":
        g_x += 1
    if g_x > 10 or g_y > 10 or g_x < 1 or g_y < 1:
        print("Wyszedłeś poza plansze")
        break
    if g_x == s_x and g_y == s_y:
        print("WYGRAŁEŚ")
        break
    min_l_ruch_po = abs(s_x - g_x) + abs(s_y - g_y)

    # określenie czy się przybliża czy oddala
    if min_l_ruch_po > min_l_ruchu_przed:
        print("Zimno")
    if min_l_ruch_po < min_l_ruchu_przed:
        print("Ciepło")

print(f"Położenie skarbu: x = {s_x}, y = {s_y}")
print(f"Połozenie gracza: x = {g_x}, y = {g_y}")
print(f'Minimalna liczba kroków do skarbu: {min_krokow_po_wylosowaniu}')
