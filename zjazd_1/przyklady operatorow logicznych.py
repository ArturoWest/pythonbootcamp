a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
# a większe od b i a podzielne przez b
print("Wynik ", a > b and a % b == 0)

# a większe od b lub > 7
print("Wynik ", a > b or a > 7)

print(not a < 10)

x = int(input("Podaj x: "))
y = int(input("Podaj y: "))

if a > b and a % b == 0:
    print(f"liczba {x} jest większa od {y} i jest przez {y} podzielna")
elif a == b:
    print("liczba x jest równa y i wynosi: {x}")
else:
    print('OK')