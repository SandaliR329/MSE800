# main.py

# Dictionary 1
student1 = {
    "name": "Alex",
    "age": 42,
    "course": "Data Analytics",
    "city": "Auckland",
    "status": "Lecturer"
}

# Dictionary 2
student2 = {
    "name": "Sophia",
    "age": 29,
    "course": "Software Engineering",
    "city": "Wellington",
    "status": "Student"
}

# Store dictionaries in a list
students = [student1, student2]

# Empty dictionary for merged result
merged_students = {}

# Merge only if name contains "ex"
for student in students:
    if "ex" in student["name"].lower():
        merged_students = {
            **merged_students,
            student["name"]: student
        }

# Print result
print("Merged Dictionary:")
print(merged_students)