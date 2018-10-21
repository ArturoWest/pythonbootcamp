#a = 3
#b = 9
#h = 6.5
#pole = ((a + b) / 2) * h
#print(f'pole trapezu o podstawach: {a}, {b} i wysokosci: {h} wynosi: {pole}')

#assert pole==39,0

def pole_trapezu(a, b, h):
    """
    Liczymy pole trapezu

    :param a: podstawa 1 - numeric
    :param b: podstawa 2 - numeric
    :param h: wysokosc - numeric
    :return: pole powierzchni - numeric
    """
    return ((a+b)/2 + h)

def test_pole_trapezu():
    assert pole_trapezu(3, 9, 6.5) == 39.0
