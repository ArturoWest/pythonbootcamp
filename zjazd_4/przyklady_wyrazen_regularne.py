import re
pattern = re.compile("\d{3}-\d{3}-\d{3}")

text = "122-222-342 321-234-567"

print(pattern.findall(text))
