
# napisz program wczytujacay liste adresow emial z pliku i tworzacy nowy plik z odfiltrowana zawartoscia
# wejscowy plik moze zawierac duplikaty adresow, ten sam adres pisany rozna wielkoscia liter
# linie zawierajace biale znaki oraz bledne adresy emial (brak znaku @ lub wystepujje on wiele razy)
# wynikowy plik powinien zawierac unikalne, posortowane, poprawne adresy emial.

# Przyklady uzycia:
# $ python clean_emails.py emials.txt cleaned_emails.txt

import sys

def validate_email(line):
    line = line.strip().lower()
    if line.count('@') == 1:
        return line


if len(sys.argv) == 3:
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    emails = set()
    with open(input_file) as f:
        for line in f:
            email = validate_emails(line)
            if email:
                emails.add(emails)
    with open(output_file) as f:
        for emails in sorted(emails):
            f.write(emails)
else:
    print("nieprawidlowa liczba parametrow")
