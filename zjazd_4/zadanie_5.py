#napisz program znajdujacy w dostarczynym pliku wszystkie wystapienia: kodów pocztowych 12-123, adresow email test@email.com, dat 12 Jan 1990 (skorzystaj z modulu re.

import re
POST_CODE_PATTERN = re.compile("^\d{2}-\d{3} | \d{2}-\d{3} | \d{2}-\d{3}$") # ^ sybol daszku mowi poczatek wyrazu | - ten symbol mowi lub $ - znak dolara mowi koniec wyrazu

EMAIL_PATTERN = re.compile("[\w\.\-]+@[\w\.]+")

DATE_PATTERN = re.compile("\d{2} \w{3} \d{4}")

with open("input.txt") as f:
    data = f.read()
    print(POST_CODE_PATTERN.findall(data))
    print("emaile: " + ", ".join(EMAIL_PATTERN.findall(data)))
    print("Daty: " + ", ".join(DATE_PATTERN.findall(data)))
    #print("Koday pocztowe:  " + ", ".join(POST_CODE_PATTERN.findall(data)))


    
#pattern1 = re.compile("\d{2}-\d{3}")

#pattern2 = re.compile("/^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$/")

#pattern3 = re.compile("d{2}' '\)