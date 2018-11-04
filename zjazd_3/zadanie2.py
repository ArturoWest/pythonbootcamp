class Product(object):
    def __init__(self, id, nazwa, cena):
        self.ID = id
        self.nazwa = nazwa
        self.cena = cena

def print_info(self):
    return f"Product {self.nazwa}, {self.ID}, {self.cena}"

print(print_info)

def test_product():
    product = Product(1, "Woda", 10.99)
    assert product.ID == 1
    assert produc.nazwa == "Woda"
    assert product.cena == 10.99

def test_product_print_info():
    product = Product(1, "Woda", 10.99)
    assert product.print_info() == 'Product "Woda", id: 1, cena:10.99 PLN'

