import json
with open("phone.json", "r") as f:
    data = json.load(f)
    print(f'model: {data['model']}')

    yanginarx=int(input('yanginarxni yozing: '))
    with open("phone.json", "w") as f:
        data['narx'] = yanginarx
        json.dump(data, f)
    print(f'yangi narx: {data["narx"]}')