class class1:# To create a class, use the keyword class:
    word1 = "This is a class"

obj1 = class1()#Now we can use the class to create objects.You can create multiple objects from the same class:
print(obj1.word1)

del obj1 # You can delete objects by using the del keyword:

class Empty:
    pass #class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.

class class2:
    def __init__(self,val1,val2,val3,val4 = 40):
        self.val1 = val1
        self.val2 = val2
        self.val3 = val3
        self.val4 = val4

obj2 = class2(10,20,30)

print("\n",obj2.val1,obj2.val2,obj2.val3,obj2.val4,"I used a _init_ method")
"""All classes have a built-in method called __init__(), which is always executed when the class is being initiated.

The __init__() method is used to assign values to object properties, or to perform operations that are necessary when the object is being created.

Without the __init__() method, you would need to set properties manually for each object:

You can also set default values for parameters in the __init__() method:"""
