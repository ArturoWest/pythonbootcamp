# zaimplementuj klase ElectricCar odzorowujaca prace samochodu elektrycznego. Klasa powinna umozliwiac pokonanie zadanego dystansu, ktory nie moze przekroczyc maksymalnego zasiagu zdf. dla samochodu. Samochod powinien miec takze molziwosc ladoawnia baterii.


# >>> car = ElectricCar(100)
# >>> car.drive(70)
# 70
# >>> car.drive(50)
# 30
# >>> car.drive(50)
# 0
# >>> car.charge()
# >>> car.drive(50)
# 50

class ElectricCar:
    def __init__(self, max_range):
        self.max_range = max_range
        self.possible_distance = max_range

    def drive(self, distance):
        if distance >= self.possible_distance:
            can_travel = self.possible_distance
            self.possible_distance = 0
            return can_travel
        self.possible_distance -= distance

        return distance

    def charge(self):
        self.possible_distance = self.max_range


def test_ElemctricCar():
    car = ElectricCar(100)
    assert car.drive(70) == 70
    assert car.drive(50) == 30
    assert car.drive(50) == 0
    car.charge()
    assert car.drive(50) == 50
    car.charge()
    assert car.drive(100) == 100