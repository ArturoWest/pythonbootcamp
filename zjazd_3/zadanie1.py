class Dog:

    def _init_(self, energy):
        self.energy = 10

    def get_energy(self):
        return self_energy
    def bark (self):
        self.energy -= 1
    def sleep(self):
        self.enegry += 2

dog = Dog()
assert dog.get_energy() == 10
dog.bark()
dog.bark()
assert dog.get_energy() == 8
dog.sleep()
assert dog.get_energy() == 10


