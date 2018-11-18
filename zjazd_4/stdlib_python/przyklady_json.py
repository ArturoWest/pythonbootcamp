import json

# tworze pythonowy obiekt

meble = ["krzesło", "szafa", "komoda", "stoł"]

print(type(meble))

meble_as_json = json.dumps(meble)
print(type(meble_as_json))
print(meble_as_json)

odczyt_z_json_as_meble = json.loads(meble_as_json)
print(type(odczyt_z_json_as_meble))
print(odczyt_z_json_as_meble)

#with open("meble.json", "w") as f:
#    json.dump(meble, f)

with open("meble.json") as f:
    meble = json.load(f)
    meble.append("taboret")
    print(meble)

with open("meble.json", "w") as f:
    json.dump(meble, f)