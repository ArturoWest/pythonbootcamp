import csv
with open('dane/titanic_train.csv') as csvfile:
    data = csv.DictReader(csvfile, delimiter=",")
    print(data)
    dlugosc = {}

    for row in data:
        print(row['Survived'])
        print(row['Sex'])
        dlugosc[row["Survived"]] = dlugosc.get(row["Survived"], 0) + 1
       # dlugosc[row[1]]= dlugosc.get(row[1], 0) + 1
        print(dlugosc)
        przezylo = dlugosc['1']
        zginelo = dlugosc['0']

    print("Przezylo z ogolu {round(100*przezylo/(przezylo+zginelo), 2)}")
    print("Zginelo z ogolu {round(100*zginelo/(przezylo+zginelo), 2)}")
    kobiety = {}

    for row in data:
        if row['Sex'] == 'female':
            kobiety[row['Survived']] = kobiety.get(row['Survived'], 0) + 1

            print("Przezylo kobiet {round(100*przezylo/(przezylo+zginelo), 2)}")

    for row in data:
        if row['Sex'] == 'male':
            mezczyzni[row['Survived']] = mezczyzni.get(row['Survived'], 0) + 1

            print("Przezylo mezczyzn {round(100*przezylo/(przezylo+zginelo), 2)}")

    with open("dane/titanic_train.csv") as csvfile:
        data = csv.DictReader(csvfile, delimiter=",")

        how_many_woman = 0
        suma_woman_age = 0

        how_many_man = 0
        suma_man_age = 0

        uniqe_age_values=set()

        for row in data:
            unique_age_values.add(row['Age'])

            if data['Sex'] =='female' and row['Age'] != "":
                how_many_woman += 1
                sum_woman_age += float(row['Age'])
            elif row['Secx'] == 'male' and row['Age'] != "":
                how_many_man += 1
                sum_man_age += float(row['Age'])

            print(f"Srednia wieku kobiet to: {sum_woman_age/how_many_woman}")
            print(f"Srednia wieku mezczyzn to: {sum_man_age/how_many_man}")

    print(uniqe_age_values)



    # oglolem przezywalnosc



# 1. policzyc % przezywalnosc wsrod ogolu, kobiet, mezczyzn

# 2. policzyc srednia wieku kobiet i mezczyzn

