#Except Handling

#Sample1

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: You can't divide by zero! Reality would collapse.")

"""Explanation: If the code inside try hits a ZeroDivisionError, Python jumps straight to the except block instead of crashing."""

print("\n")

#Sample2

try:
    num = int(input("Enter a number: "))
    result = 100 / num
except ValueError:
    print("That's not a number!")
except ZeroDivisionError:
    print("Don't use zero.")

#Explanation: This catches two distinct issues: the user typing "hello" (ValueError) or the user typing "0" (ZeroDivisionError).

print("\n")

#Sample3

try:
    import non_existent_module
except ImportError as e:
    print(f"System error caught: {e}")

"""Explanation: Using as e assigns the error details to a variable. This is great for logging exactly what went wrong."""

print("\n")

#Sample4

try:
    data = {"key": "value"}
    print(data["missing_key"])
except Exception as e:
    print(f"Something went wrong: {type(e).__name__}")

"""Explanation: Exception is the "parent" of almost all errors. It’s a safety net, but it's usually better to be specific so you don't hide bugs you didn't expect."""
print("\n")

#Sample5

try:
    val = int("10")
except ValueError:
    print("Conversion failed.")
else:
    print(f"Success! The number is {val}")

"""Explanation: This separates the "risky" code from the "success" code, making the logic cleaner."""

print("\n")

#finally

#Sample1

f = open("test.txt", "w")
try:
    f.write("Hello World")
finally:
    f.close()
    print("File closed safely.")\
        
"""Ensuring a file doesn't stay open in memory."""

print("\n")

#Sample2

def check_status():
    try:
        return "Process Finished"
    finally:
        print("I am inevitable. I run after the return!")

print(check_status())

"""finally is so persistent it even executes after a return"""

print("\n")

#Sample3

try:
    try:
        print("Nested logic...")
    finally:
        print("Inner cleanup.")
except:
    print("Outer catch.")

"""Using finally inside another handler for layered safety."""

print("\n")

#Sample4

print("\n")

#Sample5

print("\n")

#Raise

#Sample1

print("\n")

#Sample2

print("\n")

#Sample3

print("\n")

#Sample4

print("\n")

#Sample5

print("\n")