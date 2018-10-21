print("Witaj graczu, podaj pozycję swojej jednostki w zakresie od 0 do 100")
print("________________________")
x = int(input("podaj współrzędną x: "))
y = int(input("podaj współrzędną y: "))

if x > 100 or y > 100 or x < 0 or y < 0:
    print("Wypadłeś z planszy")
elif x > 90 and y > 90:
    print("Jesteś w prawym górnym rogu")
elif x > 90 and y < 10:
    print("Jesteś w prawym dolnym rogu")
elif x < 10 and y < 10:
    print("Jesteś w lewym dolnym rogu")
elif x < 10 and y < 90:
    print("Jesteś w lewym górnym rogu")
elif x < 10:
    print("Jesteś w lewej krawędzi")
elif x < 90:
    print("Jesteś na prawej krawędzi")
elif y < 10:
    print("Jesteś na dolnej krawędzi")
elif y > 90:
    print("Jesteś na górnej krawędzi")
else:
    print("Jesteś w centrum")
