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

# Dictionary 3
student3 = {
    "name": "Michael",
    "age": 35,
    "course": "Cyber Security",
    "city": "Christchurch",
    "status": "Researcher"
}

# Store all dictionaries in a list
students = [student1, student2, student3]

# Merge dictionaries if the name contains "azw"
# (case insensitive)
merged_students = {}

for student in students:
    if "Alex".lower() in student["name"].lower():
        merged_students[student["name"]] = student

# Print result
print("Merged Dictionary:")
print(merged_students)