import csv

students = [
    {"Roll no": "101", "Name": "Anitha", "Department": "CSE", "Mark": 86},
    {"Roll no": "102", "Name": "Bala", "Department": "CSE", "Mark": 91},
    {"Roll no": "103", "Name": "Chitra", "Department": "ECE", "Mark": 78}
]

course = ("Python", 4)
print("Course Tuple:", course)

with open("students.txt", "w") as file:
    for student in students:
        file.write(str(student) + "\n")

fields = ["Roll no", "Name", "Department", "Mark"]

with open("student.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    writer.writerows(students)

print("\n--- Records from CSV ---")

with open("student.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["Roll no"], row["Name"],
              row["Department"], row["Mark"])