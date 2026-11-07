import json
with open("student.json", "r") as f:
    data = json.load(f)
    data['ball'] = 95

with open("student.json", "w") as f:
    json.dump(data, f)
print(f'ball: {data["ball"]}')