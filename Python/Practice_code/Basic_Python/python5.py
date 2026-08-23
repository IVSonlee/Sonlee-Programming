a = lambda result1 : result1 & True

print("Lambda Function:", a(True))

"""A lambda function is a small anonymous function.A lambda function can take any number of arguments, but can only have one expression.

Syntax
lambda arguments : expression
The expression is executed and the result is returned:"""

b = lambda c,d : c * d

print("\nNumber of arguments using lambda",b(10,20))

"""Lambda functions can take any number of arguments:"""

def function_lambda1(word1):
    return lambda e : e + word1

lambda1_output = function_lambda1(" Functions ")
lambda_output2 = function_lambda1(" Repeated function")

print("\n"+ lambda1_output("Lambda") + lambda_output2("or use it as "))

"""The power of lambda is better shown when you use them as an anonymous function inside another function.
Or, use the same function definition to make both functions, in the same program:

Use lambda functions when an anonymous function is required for a short period of time."""

lambda_list1 = [1,2,3,4,5]

lambda_map = list(map(lambda list1_values: list1_values + 2, lambda_list1))

print("\nUsing lambda with map():",lambda_map)

"""Using Lambda with map() The map() function applies a function to every item in an iterable:"""

lambda_filter = list(filter(lambda list1_odd: list1_odd % 2 != 0 ,lambda_list1))

print("\nUsing lambda with filter:", lambda_filter)

"""The filter() function creates a list of items for which a function returns True:"""

lambda_sorted = [("Iverson",21),("Richmond",20),("Lee",19),("Abella",18)]

lambda_sorting = sorted(lambda_sorted, key=lambda a: a[1])

print("\n I am using a sorted function:",lambda_sorting)

"""The sorted() function can use a lambda as a key for custom sorting:"""

sorting_length = {'This', "time", "I", "will", "be", "different"}

len_sorting = sorted(sorting_length, key=lambda sort: len(sort))

print("\nI am using sorted function based on the length of the string:", len_sorting)

def recursion1(num):
    if num == 9:
        print("I am using a recursion")
    else:
        print(num)
        recursion1(num + 1)

recursion1(0)

"""Recursion is when a function calls itself.Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop 
through data to reach a result."""

def factorial_function(a):
    #Base case
    if a == 0:
        return 1
    #Recursive case
    else:
        return a * factorial_function(a - 2)

print("\nThis is a factorial recursion:",factorial_function(6))

"""Every recursive function must have two parts:

A base case - A condition that stops the recursion
A recursive case - The function calling itself with a modified argument
Without a base case, the function would call itself forever, causing a stack overflow error."""

def fibonacci_function(a):
    if a <= 1:
        return a
    else:
        return fibonacci_function(a - 1) + fibonacci_function(a - 2)
    
print("\nThis is a fibonacci recursion",fibonacci_function(10))

"""The Fibonacci sequence is a classic example where each number is the sum of the two preceding ones. The sequence starts with 0 and 1:
0, 1, 1, 2, 3, 5, 8, 13, ...
The sequence continues indefinitely, with each number being the sum of the two preceding ones.
We can use recursion to find a specific number in the sequence:"""