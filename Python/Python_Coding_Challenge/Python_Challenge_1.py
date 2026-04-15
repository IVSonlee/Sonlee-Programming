#Task 1

print("=====================================\nWelcome to the Student Report System\n=====================================")

#Task 2

student_name = "Maria Santos"
age = 17
grade_level = 11.0
is_enrolled = True

ladjust = " "

def function1():
    global SCHOOL_NAME 

    SCHOOL_NAME = f"""\nPythonville Academy"""

    student_profile = """School: {}
Name  : {}
Age   : {}
Grade : {}
Active: {}""".format(SCHOOL_NAME, student_name, age, grade_level, is_enrolled)

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
Remark   : \"\"""".format(original.strip(),original[1:6],original[7:13],original[1:6].capitalize(),original[7:13].upper())

print(task4)



