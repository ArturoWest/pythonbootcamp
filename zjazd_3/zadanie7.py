# zaimplementuj klasę CashMachine umożliwiającą wpłacanie i wypłacania piniędzy. Zadbaj o to abystan bankomatu przetrzymywany był w zmiennych prywatnych.
# >>> cash_machine = CashMachine()
# >>> cash_machine.is available
# False
# >>>cash_machine.put_money([200, 100, 100, 50])
# >>>cash_machine.is_available
class CashMachine:

    def __init__(self):
        self.bills = []

    def is_avaiable(self):
        if self.bills:   # return bool(self.bills)
            return True
        return False

    def put_money(self, bills):
        self.bills += bills # lub self.bills.extend(bills)

    def withdraw_money(self, amount):
        bills_to_withdraw = []
        for bill in self.bills:
            if sum(bills_to_withdraw) + bill <= amount:
                bills_to_withdraw.append(bill)
        if sum(bills_to_withdraw) == amount:
            for bill in bills_to_withdraw:
                self.bills.remove(bill)
            return bills_to_withdraw
        return []

def test_cash_machine_not_avaiable():
    cash_machine = CashMachine()
    assert not cash_machine.is_avaiable()
    assert cash_machine.is_avaiable() == False

def test_cash_machine_is_avaiable_after_put_money():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    assert cash_machine.is_avaiable() == True

def test_cash_machine_withdraw_money():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    assert cash_machine.withdraw_money(150) == [100, 50]
    assert cash_machine.withdraw_money(150) == []

def test_cash_machine_wrong_amount():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    assert cash_machine.withdraw_money(123) == []

def test_cash_machine_order_matters():
    cash_machine = CashMachine()
    cash_machine.put_money([20, 20, 50, 50])
    assert cash_machine.withdraw_money(100) == [50, 50]