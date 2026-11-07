import csv
with open('students.csv', 'r') as file:
    reader = csv.DictReader(file)
    students = list(reader)

print("Barcha o'quvchilar:")
for student in students:
    print(f" {student['ism']}")

print("20 yoshdan katta:")
for student in students:
    if int(student['yosh']) > 20:
        print(f"- {student['ism']} {student['yosh']} yosh")
