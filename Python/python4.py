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









