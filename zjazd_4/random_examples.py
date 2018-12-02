import random

random.seed(3) # teraz zawsze wylosujemy ta sama stala liczbe, kazdy wybor bedzie zawsze ten sam

print(random.random()) # zwraca losowa liczbe z zakresu 0 do 1

print(random.randint(1, 100))

print(random.randrange(1, 199))

pets = ["cat", "dog", "fish", "kuna"]

print(random.choice(pets))