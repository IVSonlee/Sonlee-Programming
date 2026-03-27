var1,var2 = "Word1",5

if len(var1) == var2:
    print(f"{len(var1)} is equal to {var2}.")

"""The if statement evaluates a condition (an expression that results in True or False). If the condition is true, 
the code block inside the if statement is executed. If the condition is false, the code block is skipped."""

if True:
    print("\nI am using boolean variables in an if statement.")

if False:

    print("This will be not displayed since its false")

#Boolean variables can be used directly in if statements without comparison operators.

if len(var1) < var2:
    print("This will be not displayed")

elif len(var1) > var2:
    print("\nI am using elif statement but this will be not displayed")

elif len(var1) == var2:
    print("\nI am using elif statement")

"""The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".

The elif keyword allows you to check multiple expressions for True and execute a block of code as soon as one of the conditions evaluates to True.

You can have as many elif statements as you need. Python will check each condition in order and execute the first one that is true.

When you use elif, Python evaluates the conditions from top to bottom. As soon as it finds a condition that is true, it executes that block and skips all remaining conditions."""


if var2 is str(var2):
    print("This will be not displayed")

elif var2 is float(var2):
    print("This will be not displayed")

elif var2 is bool(var2):
    print("This will be not displayed")
else:
    print("\nI am using a else statement")

"""The else keyword catches anything which isn't caught by the preceding conditions.

The else statement is executed when the if condition (and any elif conditions) evaluate to False.

The else statement provides a default action when none of the previous conditions are true. Think of it as a "catch-all" 
for any scenario not covered by your if and elif statements."""

print("\nI am using a shorthand if-else statement") if len(var1) == var2 else print("This will be not displayed")

#If you have one statement for if and one for else, you can put them on the same line using a conditional expression:

a = 20
b = 21

result = a if a % 2 == 0 else print("It is not divisible")

print("\nThis is how to assign a value with if else shorthad statement:",result)

#You can also use a one-line if/else to choose a value and assign it to a variable:

"""The syntax follows this pattern:

variable = value_if_true if condition else value_if_false"""

print("\nA is greater than B") if a > b else print("\nA is less than B") if a < b else print("\n")

#You can chain conditional expressions, but keep it short so it stays readable:

if a < b:
    if a % 2 == 0:
        print("\nb is greater than a and divisible by 2")

else:
    print("\n")

#You can have if statements inside if statements. This is called nested if statements.

grade = (1.0,2.0,3.0,4.0,5.0)
grade2 = (4.1,4.2,4.0,1.0)

if grade[3] is grade2[2]:
    pass
else:
    pass

#if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.

match_var = None

match match_var:
    case True:
        print("\nCase True is in match_var")
    case None:
        print("\nCase None is in match_var")
    case False:
        print("\nCase false is in match_var")
    case _:
        print("\nThis will be executed if there is no other matches")\
        
"""The match statement selects one of many code blocks to be executed.

The match expression is evaluated once.
The value of the expression is compared with the values of each case.
If there is a match, the associated block of code is executed.

Use the underscore character _ as the last case value if you want a code block to execute when there are not other matches:

"""

combine_values = "Programming"

match combine_values:
    case int(combine_values) | float(combine_values):
        print("\nThis is a int or float data type")
    case str(combine_values) | list(combine_values) if len(combine_values) == 11:
        print("\nThis is a string or a list data type with a length of index 11")
    case _:
        pass

#Use the pipe character | as an or operator in the case evaluation to check for more than one value match in one case:
#You can add if statements in the case evaluation as an extra condition-check:

start_while = 10

while start_while < 100:
    print("While Loop:",start_while)
    start_while += 10
    if start_while == 80:
        break

#With the while loop we can execute a set of statements as long as a condition is true.

#With the break statement we can stop the loop even if the while condition is true:

print("\nI am using a continue in a while loop")

even_only = 0

while even_only <= 10:
    even_only += 1
    if even_only == 5:
        continue
    print(even_only)

#With the continue statement we can stop the current iteration, and continue with the next:

print("\nI am using a continue in a for loop")

for_loop = "For Loop"

for loop1 in for_loop:
    if loop1 is "L":
        continue
    print(loop1)

print("\nI am using a break in a for loop")

"""A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc"""

for loop1 in for_loop:
    if loop1 is "L":
        break
    print(loop1)

#With the break statement we can stop the loop before it has looped through all the items:

print("\nI am using a range function in a for loop")

for iterate in range(5):
    print(iterate)

"""To loop through a set of code a specified number of times, we can use the range() function,

The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number."""

def function1():
    print("\nThis is a function from function1()")

function1()

#In Python, a function is defined using the def keyword, followed by a function name and parentheses:

#To call a function, write its name followed by parentheses:

#You can call the same function multiple times:

def function2():
    return 2026

function2()

print("\nI am using a return statement from a function:",function2())

"""Functions can send data back to the code that called them using the return statement.

When a function reaches a return statement, it stops executing and sends the result back:"""

def function3():
    pass

"""Function definitions cannot be empty. If you need to create a function placeholder without any code, use the pass statement:

The pass statement is often used when developing, allowing you to define the structure first and implement details later."""

def function4(fname,mname,lname):
    print("\nMy name is",fname,mname,lname)

function4("Iverson Richmond","Abella","Lee")

"""Information can be passed into functions as arguments.

Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

A parameter is the variable listed inside the parentheses in the function definition.

An argument is the actual value that is sent to the function when it is called.

By default, a function must be called with the correct number of arguments.

If your function expects 2 arguments, you must call it with exactly 2 arguments."""

def function5(her = "Verzosa"):
    print(her)

function5("Carrel")
function5()

#You can assign default values to parameters. If the function is called without an argument, it uses the default value:

def function6(course1,course2):
    print("\nI am using keyword arguments",course1,course2)

function6(course1 = "Information", course2 = "Technology")

#You can send arguments with the key = value syntax.

def function7(job,goal):
    print(job,"will make me",goal)

function7("trading","rich")

"""When you call a function with arguments without using keywords, they are called positional arguments.

Positional arguments must be in the correct order:"""

list1 = ["list1",10,True]
dictionary = {"dict1" : "Iverson", "dict2" : "Lee"}

def function8(list1,dictionary):
    print("\nMy name is", dictionary["dict1"],dictionary["dict2"]," I made a list:",list1)

function8(list1,dictionary)

def function9(a,b):
    return a & b
    
result1 = function9(False,True)

print("\nI am using a return at function9():",result1)

#Functions can return values using the return statement:

def function10():
    return {"dict1" : "Dictionary1","dict2" : "Dictionary2"}

result2 = function10()

print("Functions can return any data type",result2)

#Functions can return any data type, including lists, tuples, dictionaries, and more.

def function11(topic,/):
    print("\nThis is a:",topic)

function11("Positional-Only Arguments")

"""You can specify that a function can have ONLY positional arguments.

To specify positional-only arguments, add , / after the arguments:"""

def function12(*,keyword_only):
    print("\nThis is a:",keyword_only)

function12(keyword_only = "Keyword-Only Arguments")

#To specify that a function can have only keyword arguments, add *, before the arguments:

#Without *,, you are allowed to use positional arguments even if the function expects keyword arguments:

def function13(num1,num2,/,*,num3,num4):
    return num1 + num2 + num3 + num4

positional_and_keyword = function13(10,20,num3 = 30, num4 = 40)

print("\nCombining Positional-Only and Keyword-Only",positional_and_keyword)

def function14(*name):
    print("\nI am using args:",name[0],name[1],name[2])

function14("Iverson","Richmond","Lee")

"""If you do not know how many arguments will be passed into your function, add a * before the parameter name.

This way, the function will receive a tuple of arguments and can access the items accordingly:

The *args parameter allows a function to accept any number of positional arguments.

Inside the function, args becomes a tuple containing all the passed arguments:"""

def function15(positional_arg,*numbers):
    for loop in numbers:
        print(f"\n{positional_arg}:{loop}")

function15("Number",1,2,3)

"""You can combine regular parameters with *args.

Regular parameters must come before *args:"""

def function16(**kwargss):
    print("\nI am using",kwargss["asterisk"],kwargss["parameter"],"it will be received as a",kwargss["type"])

function16(asterisk = "**", parameter = "parameter name", type = "dictionary")

"""If you do not know how many keyword arguments will be passed into your function, add two asterisks ** before the parameter name.

This way, the function will receive a dictionary of arguments and can access the items accordingly:

The **kwargs parameter allows a function to accept any number of keyword arguments.

Inside the function, kwargs becomes a dictionary containing all the keyword arguments:"""

food = ("Pizza","Burger","Fries")

def function17(*argss,**kwargss):
    customer_order = f"""\nItems Ordered:
- {argss[0]}
- {argss[1]}
- {argss[2]}

Order Details:
table: {kwargss["table"]}
discount: {kwargss["discount"]}
customer: {kwargss["customer"]}"""
    
    print(customer_order)

function17(food[0],food[1],food[2],table = 5, discount = True, customer = "Alice")

"""You can combine regular parameters with **kwargs.

Regular parameters must come before **kwargs:"""

unpack_argss = ["Unpack1","Unpack2","Unpack3"]
unpack_kwargss = {"value1" : 1, "value2" : 2,"value3" : 3}

def function18(list1,list2,list3,value1,value2,value3):
    print(f"\n{value1}:{list1}\n{value2}:{list2}\n{value3}:{list3}")

function18(*unpack_argss,**unpack_kwargss)

"""The * and ** operators can also be used when calling functions to unpack (expand) a list or dictionary into separate arguments.

If you have values stored in a list, you can use * to unpack them into individual arguments:

If you have keyword arguments stored in a dictionary, you can use ** to unpack them:"""

def function18():
    outer_func = "Function Inside Function"
    def function19():
        print("\n",outer_func)
    function19()

function18()

#A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

def layer1():
    keyword = "nonlocal1"
    def layer2():
        nonlocal keyword
        def layer3():
            nonlocal keyword
            keyword = "nonlocal"
        layer3()
        return keyword
    layer2()
    return keyword

print(f"\nI am using a {layer1()} keyword")

"""The nonlocal keyword is used to work with variables inside nested functions.

The nonlocal keyword makes the variable belong to the outer function."""

def decorate(name):
    def inner_decorator():
        return name().upper()
    return inner_decorator

@decorate
def decorator_name():
    return "\nPython Decorator"

print(decorator_name())

"""Decorators let you add extra behavior to a function, without changing the function's code.

A decorator is a function that takes another function as input and returns a new function.

"""

def decorator_name2(from_decorate2):
    def inner_decorator2(*args, **kwargs):
        print(f"args: {args} | kwargs: {kwargs}")
        output_decorate2 = from_decorate2(*args, **kwargs) 
        return output_decorate2
    return inner_decorator2

@decorator_name2
def decorate2(*args, **kwargs):
    compute = sum(args) * kwargs["multiply"]
    print(f"Result: {compute}")

decorate2(1, 2, 3, 4, multiply=2)
    

"""Sometimes the decorator function has no control over the arguments passed from decorated function, to solve this problem, add (*args, **kwargs) 
to the wrapper function, this way the wrapper function can accept any number, and any type of arguments, and pass them to the decorated function"""





