sort_list = ["House","Money","Workout","Code","Sleep","Practice","aura"]

sort_list.sort()

print("Sort the list alphabetically:",sort_list)

#List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
#By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letter

sort_list.sort(reverse = True)

print("\nSort the list descending: ", sort_list)

#To sort descending, use the keyword argument reverse = True

sort_function = [90,32,80,100,10]

def function1(sorting):
    return abs(35 - sorting)

sort_function.sort(key = function1)

print("\nThe function will return a number that will be used to sort the list (the lowest number first): ",sort_function)

"""You can also customize your own function by using the keyword argument key = function.

The function will return a number that will be used to sort the list (the lowest number first):"""

sort_list2 = ["gym","programming","valorant","Sleep","Edit","study"]

sort_list2.sort(key = str.lower)

print("\nThis will sort first lower chracters: ",sort_list2)

sort_list2.reverse()

print("\nThe reverse() method reverses the current sorting order of the elements.", sort_list2)

#The reverse() method reverses the current sorting order of the elements.

copy_list2 = sort_list2.copy()

print("You can use the built-in List method copy() to copy a list.",copy_list2)

#Make a copy of a list with the copy() method

copy_list3 = list(sort_list)

print("\nAnother way to make a copy is to use the built-in method list().", copy_list3)

#Another way to make a copy is to use the built-in method list()

copy_list4 = sort_list2[:]

print("\nYou can also make a copy of a list by using the : (slice) operator.",copy_list4)

#You can also make a copy of a list by using the : (slice) operator.

list_category1 = ["Practice","Makes","You","Better"]
list_category2 = ["I","Will","Never","Expect","From","Anyone"]

join_list = list_category1 + list_category2

print("\nYou can use + operator to join two list:",join_list)

"""There are several ways to join, or concatenate, two or more lists in Python.

One of the easiest ways are by using the + operator.

Or you can use the extend() method, where the purpose is to add elements from one list to another list:"""

tuple1 = ("round brackets","unchangeable","tuple", "duplicate values")

print("\n",tuple1)

"""Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets.

A tuple can contain different data types:"""

tuple2 = ("one item",)

print("\nAdd a comma after the item to recognize it as a tuple",type(tuple2))

tuple_to_list = list(tuple2)

tuple_to_list[0] = "Changed to list"

print("\n",tuple_to_list)

tuple_to_list.append("Changed back to tuple")

tuple2 = tuple(tuple_to_list)

print("\n",tuple2)

"""Since tuples are immutable, they do not have a built-in append() method, but there are other ways to add items to a tuple.

1. Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple."""

add_at_tuple2 = ("Add tuple to a tuple",)

tuple2 += add_at_tuple2

print("\nAdd tuple to a tuple:",tuple2)

tuple_to_list = list(tuple2)
tuple_to_list.remove("Add tuple to a tuple")
tuple2 = tuple(tuple_to_list)

print("\nRemove an item from tuple to list",tuple2)

(unpack1,unpack2,unpack3,unpack4) = tuple1

print("\nExtracting values back into variables:",unpack1,unpack2,unpack3,unpack4)

#But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":

tuple4 = ("trading","eating","programming","playing","gaming")

(job,habit,task,*hobby,happiness) = tuple4

print("\nAsterisk is being added to another variable name:",habit,task,hobby,happiness)

#If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:

multiply_tuple = tuple4 * 2

print("\nI multiply the contents of the tuple:",multiply_tuple)

myset = {"set1","set2","set3"}

print("\nThis is an example of a set:",myset)

"""A set is a collection which is unordered, unchangeable*, and unindexed.

Sets cannot have two items with the same value."""

myset.add("added set")

print("\nThis is a add method:",myset)

#To add one item to a set use the add() method

set2 = {"I","Need","You"}

myset.update(set2)

print("\nTo add another set into the current set use update:",myset)

#To add items from another set into the current set, use the update() method.

#The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.)

myset.discard("You")

print("\nTo remove an item you can use remove or discard:",myset)

#To remove an item in a set, use the remove(), or the discard() method.

set3 = {"so","badly","that","I"}

print("\nI use the union method:",set2.union(set3,myset))

"""The union() and update() methods joins all items from both sets.

All the joining methods and operators can be used to join multiple sets.

When using a method, just add more sets in the parentheses, separated by commas:"""

set4 = set2 | set3 | myset

print("\nYou can use the | operator instead of the union() method:", set4)

#You can use the | operator instead of the union() method, and you will get the same result.

#When using the | operator, separate the sets with more | operators:

intersection1 = {"chest","biceps","traps","leg","core"}
intersection2 = {"biceps","eat","lean","bulk","sleep"}

print("\nThis will return a new set that only contains present in both sets:",intersection1.intersection(intersection2))

"""Keep ONLY the duplicates

The intersection() method will return a new set, that only contains the items that are present in both sets.

You can use the & operator instead of the intersection() method, and you will get the same result."""

set5 = {"set1","set2","set3","set4","set5"}

for looping in set5:
    print(looping)

set6 = {"set6","set7","set8","set9","set10"}

print("\nI am using a union set:",set5.union(set6))

#The union() and update() methods joins all items from both sets.

grouped_set = set5.union(set4,set6,set3)

print("\nThis is an example on how to join multiple sets:",grouped_set)

#Join multiple sets with the union() method

ampersand = intersection1 & intersection2

print("\nYou can use the & operator instead of the intersection() method, and you will get the same result.:",ampersand)

#You can use the & operator instead of the intersection() method, and you will get the same result.

intersection1.intersection_update(intersection2)

print("\nI Used a intersection_update method to keep ONLY the duplicates, but it will change the original set instead of returning a new set:",intersection1)

#The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.

set7 = {1,2,3}
set8 = {1,4,5}

difference = set7.difference(set8)

print("\nI used a difference method:",difference)

#The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.

minus = set7 - set8

print("\nI used a minus operator:",minus)

#You can use the - operator instead of the difference() method, and you will get the same result.

symetric_difference = set7.symmetric_difference(set8)

print("\nI used a symmetric difference",symetric_difference)

#The symmetric_difference() method will keep only the elements that are NOT present in both sets.

symetric_difference = set7 ^ set8

print("\nI used a ^ operator difference",symetric_difference)

#You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.

set8.symmetric_difference_update(set7)

print("\nI am using symmetric_difference_update:",set8)

"""The symmetric_difference_update() method updates the original set by removing items that are present in both sets, and inserting the other items.

As a shortcut, you can use the ^= operator instead, see example below"""

frozen = frozenset({"frozenset1","frozenset2","frozenset3"})
frozen2 = frozenset({"frozenset4","frozenset5","frozenset6"})

print("\nThis is a frozenset:",type(frozen),frozen)

# frozenset is an immutable version of a set.

#Being immutable means you cannot add or remove elements. 

print("\nI am using isdisjoint() method:",frozen.isdisjoint(frozen2))

#The isdisjoint() method returns True if none of the items are present in both sets, otherwise it returns False.

set9 = frozenset({20,30,40})
set10 = frozenset({10,20,30,40,50})

check_subset = set9.issubset(set10)

print("\nI am using a issubset() method:",check_subset," or you can use this <= operator: ", set9 <= set10)

"""The issubset() method returns True if all items in the set exists in the specified set, otherwise it returns False.

As a shortcut, you can use the <= operator instead, see example below."""

set11 = {"superset1","superset2","superset3","superset4","superset5"}
set12 = {"superset1","superset2","superset3"}

check_superset = set11.issuperset(set12)

print("\nI am using a issuperset() method:", check_superset," or you can use the >= or > operator: ", set11 > set12)

"""issuperset()	>=	Returns True if all items of another set is present in this set
 	            >	Returns True if all items of another, smaller set is present in this set"""

dictionary1 = {"food" : "chicken", "age" : 21 , "condition" : True}

print("\nI am using a dictionary data type:",dictionary1)
"""Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

Dictionaries are written with curly brackets, and have keys and values:"""

print("\nThis is how to access a dictionary item:",dictionary1["food"])

"""Dictionary items are presented in key:value pairs, and can be referred to by using the key name."""

y = dictionary1.get("age")

print("\nFor Accessing items I can use get():", y)

#There is also a method called get() that will give you the same result:

keys1 = dictionary1.keys()

print("\nI am using a keys method:", keys1)

#The keys() method will return a list of all the keys in the dictionary.

dictionary1["additional"] = "added"

print("\nThe list of keys at keys1 will be updated base at dictionary1:",keys1)

#The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected

values1 = dictionary1.values()

print("\nvalues() method will return all the values from a dictionary:", values1)

#The values() method will return a list of all the values in the dictionary.

dictionary1["added_value"] = 21

print("\nChanges added to the dictionary will be reflected to the value list:",values1)

#The list of the values is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the values list.

items1 = dictionary1.items()

print("\nThis will return all items in a dictionary using items() method:",items1)

#The items() method will return each item in a dictionary, as tuples in a list.

if "condition" in dictionary1:
    print("\ncondition key exists in dictionary1")

dictionary1["food"] = "Fried Rice"

print("\nThis is an example on how to change a value:",dictionary1["food"])

#You can change the value of a specific item by referring to its key name:

dictionary1.update({"condition":False})

print("\nI am using a update() method in a dictionary:",dictionary1)

"""The update() method will update the dictionary with the items from the given argument.

The argument must be a dictionary, or an iterable object with key:value pairs."""

dictionary1.update({"game":"Valorant"})

print("\nI can use update() method to add a another key:value in a dictionary",dictionary1)

"""The update() method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.

The argument must be a dictionary, or an iterable object with key:value pairs."""

dictionary1.pop("game")

print("I am using pop() method:",dictionary1)

#The pop() method removes the item with the specified key name:

dictionary1.popitem()

print("\nI am using a popitem() method:",dictionary1)

#The popitem() method removes the last inserted item

del dictionary1["additional"]

print("\nI am using a del keyword:",dictionary1)

#The del keyword removes the item with the specified key name:

dictionary1.clear()

print("\nI am using a clear() method:",dictionary1)

dictionary2 = {"job1" : "Software Developer", "job2" : "Networking", "job3" : "Web Designer"}

for loop_dict1 in dictionary2.keys():
    print(loop_dict1)

print("\n")

for loop_dict1 in dictionary2.values():
    print(loop_dict1)

print("\n")

for key,values in dictionary2.items():
    print(key,values)

"""You can also use the values() method to return values of a dictionary:

You can use the keys() method to return the keys of a dictionary:

Loop through both keys and values, by using the items() method:"""

dictionary3 = dictionary2.copy()
dictionary4 = dict(dictionary3)

print("\nI am using a copy method:", dictionary3," you can also use data type dict():",dictionary4)

#Make a copy of a dictionary with the copy() method:
#Make a copy of a dictionary with the dict() function:

nested_dictionary = {"Category1" : {"Food1" : "Sisig","Food2" : "Salad", "Food3" : "Noodles"}, "Category2" : {"Hobby1" : "Basketball", "Hobby2" : "Games", "Hobby2" : "Studying"},
                    "Category3" : {"Agent1" : "Jett","Agent2" : "Reyna", "Agent3" : "Sage"}}

print("\nThis is a nested dictionary:",nested_dictionary)

name = {"first name" : "Iverson Richmond", "last name" : "Lee"}
year_age = {"age" : 21, "year" : 2026}
location = {"street" : "Quezon City", "country" : "Philippines"}

nested_dictionary2 = {"category1" : name, "category2" : year_age, "category3" : location}

print("\n",nested_dictionary2)

#Create three dictionaries, then create one dictionary that will contain the other three dictionaries:

print("\nAccess Items in a Nested Dictionaries",nested_dictionary2["category1"]["first name"],nested_dictionary2["category1"]["last name"])

#To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary:

for keys,values in nested_dictionary.items():
    print(keys)
    for inside in values:
        print(inside," : ",values[inside])
    
keys2 = "Keys"
values2 = ("same values")

dictionary5 = dict.fromkeys(keys2,values2)

print("\n",dictionary5)

#The fromkeys() method returns a dictionary with the specified keys and the specified value.

"""Syntax
    dict.fromkeys(keys, value)
    
keys	Required. An iterable specifying the keys of the new dictionary
value	Optional. The value for all keys. Default value is None
"""

set_default_method = nested_dictionary2.setdefault("category3","locate")

print("\nI am using a set default method:",set_default_method)

"""The setdefault() method returns the value of the item with the specified key.

If the key does not exist, insert the key, with the specified value, see example below

Syntax
dictionary.setdefault(keyname, value)

keyname	        Required. The keyname of the item you want to return the value from
value	        Optional.
                If the key exist, this parameter has no effect.
                If the key does not exist, this value becomes the key's value
                Default value None"""