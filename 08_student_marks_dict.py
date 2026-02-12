# Program: Store student marks using dictionary and calculate average

student = {
    "Math": 85,
    "Science": 78,
    "English": 90
}

total = 0

for subject in student:
    total += student[subject]

average = total / len(student)

print("Marks:", student)
print("Average Marks:", average)
