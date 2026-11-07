import json
with open("product.json", "r") as f:
    data = json.load(f)
    umumiy_qiymat = data['narx'] * data['miqdor']
print(f"Mahsulot nomi: {data['nom']}")
print(f"Narxi: {data['narx']:,} so'm")
print(f"Miqdori: {data['miqdor']} dona")
print(f"Umumiy qiymati: {umumiy_qiymat:,} so'm")