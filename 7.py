import csv
with open('products.csv', 'r') as file:
    reader = csv.DictReader(file)
    products = list(reader)
maks_narx = 0
for product in products:
    nom = product['nom']
    narx = int(product['narx'])
    miqdor = int(product['miqdor'])
    umumiy_qiymat = narx * miqdor
    print(f"- {nom}: Narxi: {narx:,} so'm | soni: {miqdor} dona | Umumiy narxi: {umumiy_qiymat:,}")
    if narx > maks_narx:
        maks_narx = narx
        eng_qimmat_mahsulot = nom
print(f"Eng qimmat: {eng_qimmat_mahsulot} {maks_narx:,}")
