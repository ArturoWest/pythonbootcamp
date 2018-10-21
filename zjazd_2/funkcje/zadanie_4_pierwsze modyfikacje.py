def formatuj(*args, **kwargs):
    out = []
    for text in args:
        for k in kwargs:
            tekxt = text.replace(f'${k}', str((kwargs[k])))
        text = text.replace("$cena", str(cena))
        out.append(text)
    return "\n".join(out)


def test_formatuj():
    assert formatuj(
        10,
        'koszt cena PLN',
        'kwota cena brutto'
    ) == "koszt 10- PLN\nkwota 10 brutto"

    assert formatuj(
        10,
        'koszt $cena PLN',
        'kwota $cena brutto'
    ) == "koszt 10- PLN\nkwota 10 brutto"

    assert formatuj(
        10,
        'koszt $cena PLN',
        'kwota $cena brutto',
        'sumarycznie $cena'
    ) == "koszt 10 - PLN\nkwota 10 brutto\nsumarycznie 10"