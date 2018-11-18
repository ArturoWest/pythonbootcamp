import json
import urllib.request

with urllib.request.urlopen("http://api.nbp.pl/api/exchangerates/tables/A?format=jason") as f:
    print(f)
    kursy =json.loads(f.read())

rates = kursy[0]['rates']

for r in rates:
    print(f"- {r['code']} - {r['mid']}")


waluta = input("Jaką walutę z listy chcesz kupic?: ")
value = float(input("Ile chcesz kupić [waluta]?: "))

for r in rates:
    if r['code'] == waluta:
        result = value * r['mid']

print("płacisz", result)
