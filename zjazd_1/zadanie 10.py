print("Witaj graczu, podaj pozycję swojej jednostki w zakresie od 0 do 100")
print("________________________")
x = int(input("podaj współrzędną x: "))
y = int(input("podaj współrzędną y: "))

if x >= 90 and y >= 90:
    print("Jesteś w prawym górnym rogu planszy")
elif x <= 10 and y >= 90:
    print("Jesteś na lewym górnym rogu planszy")
elif x >= 90 and y <= 10:
    print("Jesteś na prawym dolnym rogu planszy")
elif x <= 10 and y <= 10:
    print("Jesteś na lewym dolnym rogu planszy")
elif x <= 10 and if (y > 10 and Y < 90):
    print("Jesteś na lewej krawędzi planszy")
