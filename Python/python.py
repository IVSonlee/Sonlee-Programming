print("This is python")#The Python print() function is often used to output variables.

import sys

print(sys.version)#To check the Python version of the editor, you can find it by importing the sys module:

"""Python has no command for declaring a variable.

A variable is created the moment you first assign a value to it.

Variables do not need to be declared with any particular type, and can even change type after they have been set."""

variable1 = "Iverson";
age = 20;

print()
print("Hi my name is ",variable1, "and my current age is ", age);
print

#This is a single line comment in python
"""While this one is a 
multi line comment"""

"""Python is an interpreted programming language, this means that as a developer you write Python (.py) files in a 
text editor and then put those files into the python interpreter to be executed.

Comments starts with a #, and Python will ignore them:

"""

#If you want to specify the data type of a variable, this can be done with casting.

variable1 = str("Lee")
age = int(21)

#In the print() function, you output multiple variables, separated by a comma:

print("My last name is ",variable1)
print("I will turn",age, type(age))#You can get the data type of a variable with the type() function.
print

#String variables can be declared either by using single or double quotes:
#Variable names are case-sensitive.
quote1 = 'single quote'
Quote1 = "double quote"

print()
print("This is a ",quote1)
print()

"""A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume).

Rules for Python variables:

A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords."""

variable1,variable2,variable3 = "November",5,2004 #Python allows you to assign values to multiple variables in one line:

print("This is an example on how to assign multiple variables in single line ",variable1, variable2, variable3)

variable1 = variable2 = variable3 = float(100.00)#And you can assign the same value to multiple variables in one line:

print("This is an example on how to assign same value to multiple variable")
print()

#If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.

collection = [100,200,300]

value1,value2,value3 = collection

print("This is called unpacking", value1, value2, value3)
print()

word1,word2,word3 = "This is"," +"," operator"

print(word1 + word2 + word3)#You can also use the + operator to output multiple variables:
print()

num1,num2 = 100,200

print("This will work as a mathematical operator", num1 + num2)#For numbers, the + character works as a mathematical operator:
print()

#In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:

game,year_release = "Valorant",2020

print(game, year_release)
print()

function = "This is a function"

def function1():print(function)#Variables that are created outside of a function

function1()

def function2():#If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function.
    global global_variable #To create a global variable inside a function, you can use the global keyword.If you use the global keyword, the variable belongs to the global scope:
    global_variable = "Global variable"
    function2 = "local variable"
    print("This is a", function2)

function2()

print(global_variable)
print()

"""Python has the following data types built-in by default, in these categories:

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType"""

datatype_complex = complex(2j)
datatype_list = list(("list1","list2","list3"))
datatype_tuple = tuple(("tuple1","tuple2","tuple3"))
datatype_range = range(10)
datatype_dict = dict(programming_language = "Python", subject = "Programming")
datatype_set = set(("set1","set2","set3"))
datatype_frozenset = frozenset(("frozenset1","frozenset2","frozenset3"))
datatype_bool = bool(10)
datatype_byte = bytes(3)
datatype_bytearray = bytearray(3)
datatype_memoryview = memoryview(bytes(10))

#To verify the type of any object in Python, use the type() function:

print("Datatype complex: ",datatype_complex," type: ", type(datatype_complex))
print("Datatype list: ",datatype_list," type: ", type(datatype_list))
print("Datatype tuple: ",datatype_tuple, "type: ", type(datatype_tuple))
print("Datatype range: ",datatype_range, "type: ", type(datatype_range))
print("Datatype dict: ",datatype_dict, "type: ", type(datatype_dict))
print("Datatype set: ",datatype_set, "type: ", type(datatype_set))
print("Datatype frozenset: ",datatype_frozenset, "type: ", type(datatype_frozenset))
print("Datatype bool: ",datatype_bool, "type: ", type(datatype_bool))
print("Datatype byte: ",datatype_byte, "type: ", type(datatype_byte))
print("Datatype bytearray: ",datatype_bytearray, "type: ", type(datatype_bytearray))
print("Datatype memoryview: ",datatype_memoryview, "type: ", type(datatype_memoryview))

integer = int(12332431232)#Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.

print()
print(integer)
    
decimal1 = 10e3 #Float can also be scientific numbers with an "e" to indicate the power of 10.

print("I indicate the power of 3 by including a", decimal1)
print()

complex_num = 20j

print("This is a complex number: ",complex_num)#Complex numbers are written with a "j" as the imaginary part:

conversion1 = 100

conversion1 = float(conversion1)

print()
print("I convert int to float ", conversion1)

conversion1 = complex(conversion1)#You cannot convert complex numbers into another number type.

print("I'll convert it from float to complex ", conversion1)
print()

import random

print(random.randrange(1,20))
"""Python does not have a random() function to make a random number, but Python has a built-in module called random that 
can be used to make random numbers""" 
print()

print('I am using a single quote')#Strings in python are surrounded by either single quotation marks, or double quotation marks.
print('I will be using a quote inside another "quote"')
print("I will be using a quote inside another 'quote'")

string1 = "This is how to assign a string"#You can assign a multiline string to a variable by using three quotes:
multi_line_string = """This is how you 
assign a multiline
string"""

print()
print(multi_line_string)
print()

string2 = "This is how to access an element of a string"

print(string2[0],string2[1],string2[2],string2[3])
"""Like many other popular programming languages, strings in Python are arrays of unicode characters.
However, Python does not have a character data type, a single character is simply a string with a length of 1.
Square brackets can be used to access elements of the string."""

#Get the character at position 1 (remember that the first character has the position 0):

print()
for word4 in "Looooping": print(word4)#Since strings are arrays, we can loop through the characters in a string, with a for loop.

length_string = "This will measure the length of the string"

print()
print(len(length_string))#The len() function returns the length of a string:

string_check = "This will check if the word check is present in this string"

print()
print("check" in string_check)#To check if a certain phrase or character is present in a string, we can use the keyword in.

characters = set((1,2,3,4,5,6,7,8,9,10))

if 10 in characters: print("Yes number 10 is included in the set")#Use it in an if statement:

string_check2 = "I will be using not in to check if that phrase or word is not included in string"

print()
print("phrase" not in string_check2)#To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.

print()
if 2 in characters: print("Number 2 is included in characters")
if 12 not in characters: print("Number 12 is not included in characters")

slicing_strings = str("String slicing")

print()
print(slicing_strings[0:10])
#You can return a range of characters by using the slice syntax.Specify the start index and the end index, separated by a colon, to return a part of the string.
#The first character has index 0.

print(slicing_strings[:6])#By leaving out the start index, the range will start at the first character:
print(slicing_strings[7:])#By leaving out the end index, the range will go to the end:
    
negative_indexing = "Negative"

print()
print(negative_indexing[-8:-4])#Use negative indexes to start the slice from the end of the string:

uppercase = "this will turn to uppercase"

print()
print(uppercase.upper())#The upper() method returns the string in upper case:
print()

lowercase = "THIS WILL TURN TO LOWERCASE"

print(lowercase.lower())#The lower() method returns the string in lower case:

remove_whitespace = "    this will remove whitespace"

print()
print(remove_whitespace.strip())#Whitespace is the space before and/or after the actual text, and very often you want to remove this space.

replace = "I will be using replace"

print()
print(replace.replace("i","e"))#The replace() method replaces a string with another string:

split_string = "This is split string"

print()
print(split_string.split(" "))#The split() method returns a list where the text between the specified separator becomes the list items.

string1,string2 = "String","Concatenation"
combine_string = string1 + " " + string2 #To concatenate, or combine, two strings you can use the + operator.

print()
print(combine_string)

f_string = 2025

code = f"I made this code around year {f_string}"#But we can combine strings and numbers by using f-strings or the format() method!

"""F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.

To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations."""

print()
print(code)

modify = 135.89

placeholder = f"I will turn float into a int {modify:.0f}"
"""A placeholder can include a modifier to format the value.

A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals"""

print()
print(placeholder)
print()

compute1,compute2 = 100,200

placeholder_operation = f"{compute1} + {compute2} = {compute1 + compute2}"#A placeholder can contain Python code, like math operations:

print(placeholder_operation)
print()
#An escape character is a backslash \ followed by the character you want to insert.
escape_characters = """This is a \"double quote\"
This is a \'single quote\'
This is a \\backslash\\
This is a new \n line
This is a \r carriage return
This is a \t tab
This is a \bbackspace
This is a \f form feed
"""
print(escape_characters)

capitalize = "capitalize the first character"

print("\n",capitalize.capitalize())#The capitalize() method returns a string where the first character is upper case, and the rest is lower case.

casefold = "This WILL CONVERT THE STRING TO LOWERCASE"

print("\n",casefold.casefold())
"""The casefold() method returns a string where all the characters are lower case.This method is similar to the lower() method, but the casefold() 
method is stronger, more aggressive, meaning that it will convert more characters into lower case, and will find more matches when comparing two strings 
and both are converted using the casefold() method."""

center = "Return center string"

print(center.center(50,"-"))#The center() method will center align the string, using a specified character (space is default) as the fill character.
#Syntax     string.center(length, character)
"""Parameter	Description
length	        Required. The length of the returned string
character	    Optional. The character to fill the missing space on each side. Default is " " (space)"""

count = "This will count the number of times it appears in this string 123123123123"

print("\n",count.count("123"),count.count("123",65,73))#The count() method returns the number of times a specified value appears in the string.
#Syntax string.count(value, start, end)
"""Parameter	Description
    value	    Required. A String. The string to value to search for
    start	    Optional. An Integer. The position to start the search. Default is 0
    end	        Optional. An Integer. The position to end the search. Default is the end of the string
"""

encode = "This will encode"

print("\n", encode.encode(),"\n",encode.encode(encoding="utf-8", errors="replace"))

#The encode() method encodes the string, using the specified encoding. If no encoding is specified, UTF-8 will be used.
#Syntax: string.encode(encoding=encoding, errors=errors)
"""
Parameter	                Description
encoding	                Optional. A String specifying the encoding to use. Default is UTF-8
errors	                    Optional. A String specifying the error method. Legal values are:


'backslashreplace'	-       uses a backslash instead of the character that could not be encoded
'ignore'	        -       ignores the characters that cannot be encoded
'namereplace'	    -       replaces the character with a text explaining the character
'strict'	        -       Default, raises an error on failure
'replace'	        -       replaces the character with a questionmark
'xmlcharrefreplace'	-       replaces the character with an xml character"""

endswith = "This will check if the text will endswith"

print("\n", endswith.endswith("h"),"\n",endswith.endswith("text",23,27),"\n", endswith.endswith(("end","endswith")))#The endswith() method returns True if the string ends with the specified value, otherwise False.
#Syntax:  string.endswith(value, start, end)
"""Parameter	Description
    value	    Required. The value to check if the string ends with. This value parameter can also be a tuple, then the method returns true if the string ends with any of the tuple values.
    start	    Optional. An Integer specifying at which position to start the search
                end	Optional. An Integer specifying at which position to end the search"""

expandtabs = "E\tx\tp\ta\tn\td"  #Set the tab size

print("\n",expandtabs.expandtabs(2))
"""The expandtabs() method sets the tab size to the specified number of whitespaces.

Syntax: string.expandtabs(tabsize)
tabsize	        Optional. A number specifying the tabsize. Default tabsize is 8"""

find = "1234589"

print("\n", find.find("4"),find.find("5",4))
"""The find() method finds the first occurrence of the specified value.

The find() method returns -1 if the value is not found.

The find() method is almost the same as the index() method, the only difference is that the index() method raises an exception if the value is not found.

Syntax:     string.find(value, start, end)

Parameter	Description
value	    Required. The value to search for
start	    Optional. Where to start the search. Default is 0
end	        Optional. Where to end the search. Default is to the end of the string"""

age = 20
month = 4

format_string1 = "\nI am turning {age} this november"
format_string2 = "\nI am turning {age} this november {month}".format(age = 21, month = 5)
format_string3 = "\nI really like {} so {}".format("her", "much")

print(format_string1.format(age = 21)+format_string2+format_string3)
"""The format() method formats the specified value(s) and insert them inside the string's placeholder.
The placeholder is defined using curly brackets: {}.The format() method returns the formatted string."""

find_index = "Find the word rich and trading in this string"

print("\nI use the index method to find the word rich and trading:",find_index.index("rich"),"and",find_index.index("trading",23,30))

"""The index() method finds the first occurrence of the specified value.

The index() method raises an exception if the value is not found.

The index() method is almost the same as the find() method, the only difference is that the find() method returns -1 if the value is not found."""

check_isalnum = "alphanumeric"

print("\ncheck_isalnum using isalnum method",check_isalnum.isalnum())

"""The isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).
Example of characters that are not alphanumeric: (space)!#%&? etc."""

check_isalpha = "ABCDE12"

print("\nI used isalpha to check is of characters is letters:",check_isalpha.isalpha())

"""The isalpha() method returns True if all the characters are alphabet letters (a-z).

Example of characters that are not alphabet letters: (space)!#%&? etc"""

check_ascii = check_isalpha

print("\nI used isascii method:",check_ascii.isascii())

#The isascii() method returns True if all the characters are ascii characters  (a-z).

check_decimal = "145"

print("\nI used isdecimal to check if the characters is decimal", check_decimal.isdecimal())

"""method returns True if all the characters are decimals (0-9).

This method can also be used on unicode objects."""

check_digit = check_decimal

print("\nI used isdigit if all the characters are digits",check_decimal.isdigit())

identifier1 = "Identifier1nospaces"
identifier2 = "1Identifierstartswithanumber"
identifier3 = "Identifier with space"

print("\nThis will check if this is an identifier:",identifier1.isidentifier(),identifier2.isidentifier(),identifier3.isidentifier())

"""The isidentifier() method returns True if the string is a valid identifier, otherwise False.

A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). A valid identifier cannot start with a number, or contain any spaces."""

lower_characters = "this will check if all the characters are in lowercase"

print("\nCheck if all the characters are in lowercase:",lower_characters.islower())

"""The islower() method returns True if all the characters are in lower case, otherwise False.

Numbers, symbols and spaces are not checked, only alphabet characters."""

numeric = "123123"
numeric2 = "123.45"

print("\nCheck if all characters in the text are numeric:",numeric.isnumeric(),numeric2.isnumeric())

printable1 = "Is it printable"

print("\nCheck if this is printable:",printable1.isprintable())

"""The isprintable() method returns True if all the characters are printable, otherwise False.

Example of none printable character can be carriage return and line feed."""

whitespace1 = "  "

print("\nCheck if all characters are whitespace:",whitespace1.isspace())

title1 = "Title"

print("\nCheck if the first character start with the first character is uppercase:",title1.istitle())

join_method = ("Join1","Join2","Join3")

grouping = "|".join(join_method)

print("\nI am using a join method:",grouping)

ljust_method = "LJust"

x = ljust_method.ljust(30)

print("\n",x, "this is an example of left adjustment")