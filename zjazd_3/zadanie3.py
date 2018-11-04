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
        return self.worked_hours # tego nie było

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

