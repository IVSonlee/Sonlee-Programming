print(12.34 > 13)
"""In programming you often need to know if an expression is True or False.You can evaluate any expression in Python, and get one of two answers, True or False.
When you compare two values, the expression is evaluated and Python returns the Boolean answer"""

val1 = val2 = 100

if val1 == val2: print("\n",val1," and ",val2," are equal")
else:print("\n",val1," and ",val2," are not equal")

print("\n",bool("If the string is empty then it will only be false and if the value is 0 it will be false also"),bool(""),bool(1),bool(0),bool(("set1","set2","set3")),bool(None))
"""Almost any value is evaluated to True if it has some sort of content.
Any string is True, except empty strings.
Any number is True, except 0.
Any list, tuple, set, and dictionary are True, except empty ones.
In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None. 
And of course the value False evaluates to False.
The following will return False:

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})"""

#You can execute code based on the Boolean answer of a function:
def function1():
    return False

if function1() == bool(1): print("\nFunction1 returns true")
else:print("\nFunction1 returns false")

print("\nThis will check the instance: ",isinstance(function1(),bool))
#Python also has many built-in functions that return a boolean value, like the isinstance() function, which can be used to determine if an object is of a certain data type:

values = [100,200,300,400]

def addition():
    global add
    add = f"\nThis is a addition {values[0] + values[1] + values[2] + values[3]}"
    print(add)

def subtraction():
    global subtract
    subtract = f"\nThis is a subtraction {values[0] - values[1] - values[2] - values[3]}"
    print(subtract)

def multiplication():
    global multiply
    multiply = f"\nThis is a multiplication {values[0] * values[1] * values[2] * values[3]}"
    print(multiply)

def division():
    global divide
    divide = f"This is a division {int(values[1] / values[0])}"
    print(divide)

def modulus():
    global remainder
    remainder = f"This is getting the remainder {int(values[1] % values[0])}"
    print(remainder)

def exponentation():
    exponent = 3
    global result
    result = f"This is exponentation {values[0] ** exponent}"

def floor_division():
    divide = values[1] // values[0]
    global floor_divide
    floor_divide = f"This is a floor division {divide}"
    

addition() 
subtraction()
multiplication()
division()
modulus()

exponentation()
print(result)
floor_division()
print(floor_divide)
"""
Operator	Name	            Example	
+	        Addition	        x + y	
-	        Subtraction	        x - y	
*	        Multiplication	    x * y	
/	        Division	        x / y	
%	        Modulus	            x % y	
**	        Exponentiation	    x ** y	
//	        Floor division	    x // y"""

def assignment_operators():
    values[0] += values[1]

    print("I am using a += operator",values[0])

    values[0] -= values[1]

    print("I am using a -=",values[0])

    values[0] *= values[1]

    print("I am using a *=", values[0])

    values[0] /= values[1]

    print("I am using /=", values[0])

    values[1] %= values[0]

    print("I am using *=", values[1])

    values1 = [1,2,3,4,5]

    values1[3] //= values1[1]

    print("I am using a //= operator", values1[3])

    values1[2] **= values1[1]

    print("I am using a **= operator",values1[2])

print("\n")
assignment_operators()

"""Assignment operators are used to assign values to variables:

Operator	Example	        Same As	
=	        x = 5	        x = 5	
+=	        x += 3	        x = x + 3	
-=	        x -= 3	        x = x - 3	
*=	        x *= 3	        x = x * 3	
/=	        x /= 3	        x = x / 3	
%=	        x %= 3	        x = x % 3	
//=	        x //= 3	        x = x // 3	
**=	        x **= 3	        x = x ** 3	
&=	        x &= 3	        x = x & 3	
|=	        x |= 3	        x = x | 3	
^=	        x ^= 3	        x = x ^ 3	
>>=	        x >>= 3	        x = x >> 3	
<<=	        x <<= 3	        x = x << 3	
:=	        print(x := 3)	x = 3
                            print(x)"""

comparison_operators = f"""I am using a == operator: {10 == 10}
I am using a != operator: {10 != 9}
I am using a > operator: {10 > 9}
I am using a < operator: {10 < 9}
I am using a >= operator: {10 >= 10}
I am using a <= operator: {10 <= 9}"""

print("\n"+comparison_operators)

"""Comparison operators are used to compare two values:

Operator	Name	                    Example	
==	        Equal	                    x == y	
!=	        Not equal	                x != y	
>	        Greater than	            x > y	
<	        Less than	                x < y	
>=	        Greater than or equal to	x >= y	
<=	        Less than or equal to	    x <= y"""

print("\nI am using a and operator to check if both statements are true", (10 > 9 and 9 <12))
print("I am using a or operator to check if one of the statements is true", (8 > 9 and 9 < 8))
print("I am using a not operator which reverse the result", not(8 > 9 and 9 < 8))

"""Logical operators are used to combine conditional statements:

Operator	Description	Example	                                            Try it
and 	    Returns True if both statements are true	                    x < 5 and  x < 10	
or	        Returns True if one of the statements is true	                x < 5 or x < 4	
not	        Reverse the result, returns False if the result is true	        not(x < 5 and x < 10)"""

obj1,obj2,obj3 = 10,10,20

print("\nI am using a is operator:", obj1 is obj2, obj2 is obj3)
print("I am using a is not operator:", obj1 is not obj2, obj2 is not obj3)

"""Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

Operator	Description	                                            Example	        Try it
is 	        Returns True if both variables are the same object	    x is y	
is not	    Returns True if both variables are not the same object	x is not y"""

def membership_operators():
    global membership  
    membership = [11,30,"120"]

membership_operators()

print("\n")
print(30 in membership,120 in membership, "120" in membership)
print(30 not in membership,120 not in membership, "120" not in membership)

"""Membership operators are used to test if a sequence is presented in an object:

Operator	Description	                                                                        Example	
in 	        Returns True if a sequence with the specified value is present in the object	    x in y	
not in	    Returns True if a sequence with the specified value is not present in the object	x not in y"""

print("\nI am using a AND operator which sets each bit to 1 if both bits are 1:", 7 & 9)
print("I am using a OR operator which sets each bit to 1 if one of the bits are 1:", 7 | 9)
print("I am using a XOR operator which sets each bit to 1 if only one of two bits is 1 :", 7 ^ 9)
print("I am using a NOT operator which inverts all the bits :", ~7)
print("Shift left by pushing zeros in from the right and let the leftmost bits fall off :", 5 << 2)
print("Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off:", 7 >> 2)

"""Bitwise operators are used to compare (binary) numbers:

Operator	Name	                Description	Example	Try it
& 	        AND	                    Sets each bit to 1 if both bits are 1	x & y	
|	        OR	                    Sets each bit to 1 if one of two bits is 1	x | y	
^	        XOR	                    Sets each bit to 1 if only one of two bits is 1	x ^ y	
~	        NOT	                    Inverts all the bits	~x	
<<	        Zero fill left shift    Shift left by pushing zeros in from the right and let the leftmost bits fall off	x << 2	
>>	        Signed right shift	    Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	x >> 2"""

list1 = ["tuple","set","dictionary"]

print("\nThis are exaple of lists: ",list1,list1[0],list1[1],list1[2])
"""Lists are used to store multiple items in a single variable.
Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
Lists are created using square brackets:
ist items are ordered, changeable, and allow duplicate values.
List items are indexed, the first item has index [0], the second item has index [1] etc.
When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
If you add new items to a list, the new items will be placed at the end of the list.
The list is changeable, meaning that we can change, add, and remove items in a list after it has been created."""

print("This will determine the number of items a list have",len(list1))
"""To determine how many items a list has, use the len() function:"""

list2 = [True,972025,"Hello"]#A list can contain different data types:

print("\n",list2)

"""There are four collection data types in the Python programming language:

List        is a collection which is ordered and changeable. Allows duplicate members.
Tuple       is a collection which is ordered and unchangeable. Allows duplicate members.
Set         is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary  is a collection which is ordered** and changeable. No duplicate members."""

print("\nGetting a list base in index number: ",list2[0],list2[-2])
#List items are indexed and you can access them by referring to the index number:
#Negative indexing means start from the end

range_index = ["This","is","a","range","of","index"]

print("\nI am displaying a specific range of index",range_index[3:6],range_index[:3])

"""You can specify a range of indexes by specifying where to start and where to end the range.

When specifying a range, the return value will be a new list with the specified items."""

if "range" in range_index[4:6]:print("\nThe word range is between index 4 - 6")
else: print("\nThe word range doesnt belong to index 4 - 6")

#To determine if a specified item is present in a list use the in keyword

change_list = [1,2,3,4,5,6,7,8,9,10]

change_list[0] = "one"#To change the value of a specific item, refer to the index number:
 
print(change_list[0])

change_list[1:4] = ["two","three","four"]
#To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:

print(change_list)

change_list[0:1] = [1,2,3]
#If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:

print("\nIf you insert more items than you replace, the new items will be inserted where you specified: ",change_list)

change_list2 = [10,20,30,40,50]

change_list2[0:4] = [0,5]#If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:

print("\nIf you insert less items than you replace, the new items will be inserted where you specified: ",change_list2)

change_list2.insert(5,60)

print("\nI am using a insert: ",change_list2)
"""To insert a new list item, without replacing any of the existing values, we can use the insert() method.

The insert() method inserts an item at the specified index:"""

change_list2.append("append")

print("\n",change_list2)

change_list.extend(change_list2)

print("\nI am using extend list: ",change_list)
"""To append elements from another list to the current list, use the extend() method.
The elements will be added to the end of the list.
The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.)."""

change_list.remove(change_list[3])#If there are more than one item with the specified value, the remove() method removes the first occurrence:

print("\nI am using a remove method: ", change_list)

change_list.pop(3)

print("\n I am using a pop method: ", change_list)#The pop() method removes the specified index.

change_list.pop()#If you do not specify the index, the pop() method removes the last item.

print("Using pop without specifying the index: ",change_list)

del change_list[10]#The del keyword also removes the specified index:

print("\nI am using a del keyword: ",change_list)

del change_list #The del keyword can also delete the list completely.

#print("This will delete the entire list: ", change_list)

change_list2.clear()#The clear() method empties the list.The list still remains, but it has no content.

print("I am using a clear method",change_list2)

looping_list = ["This","is","how","to","use","for loop","in","list"]

for loop in looping_list:
    print(loop)


    







