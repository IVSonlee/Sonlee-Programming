#Student Basics

from mimetypes import init


school_name = "Python Academy"

student_name,age,gpa = "Alex Rivera",19,3.85

is_enrolled = True

student_profile = f"""School {school_name}
Student: {student_name}
Age: {age}
GPA: {gpa}
Type of age: {type(age)}
Type of gpa {type(gpa)}
Enrolled: {is_enrolled}"""

print(student_profile,"\n\n")

#Grade Calculator

scores = "88","92","76","95","84"
casted_scores = []

for casting in scores:
    casted_scores.append(int(casting))

start = 0

for add in casted_scores:
    start += add

average = start / len(casted_scores)

grades = f"""Scores (int): {casted_scores}
Average: {average}
Above 85: {True if average > 85 else False}
Above 90: {True if average > 90 else False}
10-point band: {average // 10:.0f}"""

print(grades,"\n\n")

#Name & ID Processing

casting_age = str(age)

name_id_processing = f"""First name: {student_name[0:4]}
Student ID: {student_name[0:3] + casting_age}
Welcome: \"Hello, {student_name}! Your GPA is {gpa} at {school_name}.\"\nRecord: Student \"{student_name}\" - on file
Lowercase: {student_name.casefold()}
Uppercase: {student_name.upper()}
Replaced: {student_name.replace("Rivera","Santos")}
Count of \'a\': {student_name.count("a") + student_name.count("A")}
Stripped: {student_name.strip()}
Split: {student_name.split(" ")}"""

print(name_id_processing)

#Course List Manager

initial = ['Math','Science','English','History']

access = f"\n\nFirst: {initial[0]} | Last: {initial[3]} | Middle: {initial[1],initial[2]}"

print(access)

initial[2] = "Literature"

print(f"After change: {initial}")

initial.append("Python")
initial.insert(2,"Art")

print(f"After add: {initial}")

initial.remove("History")
initial.pop()
del initial[0]

print(f"After remove: {initial}\n\n")

print("Course by index".center(21,"-"))

length = []

for loop in range(len(initial)):
    print(loop,":",initial[loop])

    length.append(len(initial[loop]))

print(f"\nName lengths: {length}")

initial.sort()

print(f"Sorted A-Z: {initial}")

initial.sort(reverse=True)

print("Sorted Z-A:",initial)

initial.sort(reverse=False)

print("Original:",initial)

copy = ["PE"]

copy.copy(initial)

print("Copy with PE")