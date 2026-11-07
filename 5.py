import json
talaba = {
    "ism": "Sardor",
    "yosh": 20,
    "kurs": 2
}
json_matn = json.dumps(talaba, indent=10 )

print("JSON matn ko'rinishi:")
print(json_matn)

qaytadict = json.loads(json_matn)

print(f"Talaba {qaytadict['ism']}")
