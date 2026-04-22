#Task 1

from re import sub


print("=====================================\nWelcome to the Student Report System\n=====================================")

#Task 2

student_name = "Maria Santos"
age = 17
grade_level = 11.0
is_enrolled = True

ladjust = " "

def function1():
    global SCHOOL_NAME 
    global casting_grade_level
    casting_grade_level = int(grade_level)

    SCHOOL_NAME = f"""\nPythonville Academy"""

    student_profile = """School: {}
Name  : {}
Age   : {}
Grade : {}
Active: {}""".format(SCHOOL_NAME, student_name, age, casting_grade_level, is_enrolled)

    print(student_profile)

function1()

#Task 3

num1,num2,num3,num4,num5 = 88, 92, 75, 60, 84

total = num1 + num2 + num3 + num4 + num5

average = str(total)

average  = int(average) / 5

int_casting = int(average)

scores = "\nScores : {} {} {} {} {}\nTotal  : {}\nAverage: {}\nPassed : {}".format(num1,num2,num3,num4,num5,total,int_casting,True if int_casting >= 75 else False)

print(scores)

#Task 4

original = " maria santos "

task4 = """\nOriginal : \" {} \"
Sliced   : First=\"{}\" Last=\"{}\"
Formatted: \"{} {}\"
Remark   : \"\"
Contains \'a\': {} times""".format(original.strip(),original[1:6],original[7:13],original[1:6].capitalize(),original[7:13].upper(),original.count("a"))

remove_whitespace= original.strip()

print(task4,"\n\'santos\' found at index:",remove_whitespace.index("santos"))

#Task 5

subjects = ["Math","Unknown","Science","Filipino","History"]

access = " Access "

print("\n",access.center(14,"-"),f"\nFirst  : {subjects[0]}\nLast  : {subjects[4]}\nMiddle: {subjects[2]}")

subjects[1] = "Data Science"
access = " After change "

print(f"\n{access.center(20,"-")}\n{subjects}")

access = " After add "

subjects.append("PE")
subjects.insert(2,"Ethics")

print(f"\n{access.center(20,"-")}\n{subjects}")

access = " After remove & pop "

subjects.remove("History")
subjects.pop()
subjects_copy2 = subjects

print(f"\n{access.center(26,"-")}\n{subjects}\n")

[print(f"{loop}: {subjects[loop]}") for loop in range(len(subjects))]

seven_above = []

for loop2 in subjects:
    if len(loop2) > 7:
        seven_above.append(loop2)

access = " Long name subjects (>7 chars) "

print(f"\n{access.center(37,"-")}\n{seven_above}")

access = " Sorted (A→Z) "

subjects.sort()

print(f"\n{access.center(20,"-")}\n{subjects}")

subjects.reverse()

access = " Reverse sorted (Z→A) "

print(f"\n{access.center(28,"-")}\n{subjects}")

subjects_copy = subjects

access = " Backup copy "

print(f"\n{access.center(20,"-")}\n{subjects_copy}")

subject2 = ["MAPEH","TLE"]

access = " Joined List "

subjects.extend(subject2)

print(f"\n{access.center(20,"-")}\n{subjects}")

access = " Methods "

print(f"\n{access.center(20,"-")}\n\'{subjects[1]}\' appears : {subjects.count("Math")} time\n\'{subjects[2]}\' index: {subjects.index("Filipino")}\n")

average = int(average)

report_card = """╔══════════════════════════════════════╗
║   PYTHONVILLE ACADEMY — REPORT CARD ║
╚══════════════════════════════════════╝

Student  : {} {}
Age      : {}\tGrade Level: {}
Enrolled : {}

Subjects : {}
Score : {}  {}  {}  {}  {}
Average : {}      Status : Passed
Remark : {} {} showed consistent effort""".format(original[1:6].capitalize(),original[7:13].upper(),age,casting_grade_level,is_enrolled," | ".join(subjects_copy2),num1,num2,num3,num4,num5,average,original[1:6].capitalize(),original[7:13].upper())

print(report_card)

 