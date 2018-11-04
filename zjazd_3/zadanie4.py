class Employee:
    def __init__(self, imie, nazwisko, stawka):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stawka = stawka
        self.worked_hours = 0

    def pay_salary(self):
        if self.worked_hours <= 8:
            to_pay = self.worked_hours * self.stawka
        else:
            to_pay = 8 * self.stawka + (self.worked_hours - 8) * 2
        self.worked_hours = 0
        return to_pay

    def register_time(self, hours):
        self.worked_hours += hours

class PremiumEmployee(Employee):
    def _init(self, imie, nazwisko, stawka):
        super().__init__(imie, nazwisko, stawka) # wez z kalsy nadrzednej to co jest definiowane przez
        #Employee.__init__(imie, nazwisko, stawka)
        self.bonus = 0


    def givee_bonus(self, amount):
    self.bonus = amount

    def pay_salary(self):
        to_pay = super().pay_salary()           # wez z kalsy nadrzednej to co jest definiowane przez
        return to_pay + self.bonus

    def register_time(self, hours):
        self.worked_hours += hours
    def __str__(self):
# Utwórz klasę Company, którą inicjalizuję się z nazwą

class Company():
    def _init_(self, name):
        self.name = name
        self.emplyees = set()

    def add_employee(selfself, employee):
        self.employess.add(employee)

    def size(self):
        return len(self.employees)
    def pay_all_salary(self):
        sum = 0
        for e in self.employees:
            sum_ += e.pay_salary()  #e.pay_salary() - wywoluje metode pay salary dla obiektu/instancji e e to jest intancja klasy employee
        return sum_

def test_company():
    employee = Employee('Jan', "Nowak', 100)
    employee.register_time(5)
    google = Company("google")
    google.add_employee(employee)
    assert goolge.size() == 1
    assert google.pay_all_salary() == 500
    assert google.pay_all_salary() == 0
    employee2 = Employee('Krzysztof', 'Nowak', 200)
    employee2.register_time(5)
    employee.register_time(5)
    #google.pay_all_salary()
    google.add_employee(employee2)
    assert google.pay_all_salary() == 2200


def tests_employee():
   employee = Employee('Jan', "Nowak", 100)
   assert employee.imie == "Jan"
   assert employee.nazwisko == "Nowak"
   assert employee.stawka == 100

def test_employee_pay_salary():
   employee = Employee('Jan', "Nowak", 100)
   assert employee.pay_salary() == 0

def test_employee_pay_salary_with_no_worked_hours():
   employee = Employee('Jan', "Nowak", 100)
   employee = register_time(0)
   assert employee.pay_salary() == 0

def test_employee_pay_salary_with_worked_hours():
   employee = Employee('Jan', "Nowak", 100)
   employee = register_time(5)
   assert employee.pay_salary() == 500


def test_employee_pay_salary_with_worked_overhours():
   employee = Employee('Jan', "Nowak", 100)
   employee = register_time(12)
   assert employee.pay_salary() == 1600

def test_premium_employee_pay_salary_with_bonus():
    employee = PremiumEmployee('Jan', "Nowak", 100)
    employee = register_time(12)
    employee = give_bonus(1000)
    assert employee.pay_salary() == 2100

def test_premium_employee_pay_salary_without_bonus():
    employee = PremiumEmployee('Jan', "Nowak", 100)
    employee = register_time(5)
    assert employee.pay_salary() == 500

def test_company():