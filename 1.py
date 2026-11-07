import json 
with open("user.json", "r") as f:
    data = json.load(f)
    print(f"Ismi: {data['ism']}")
print(f"Yoshi: {data['yosh']}")
print(f"Shahri: {data['shahar']}")