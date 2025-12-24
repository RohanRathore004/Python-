'''
Access Modifier - Access Modifier in python we use of this for making variable public, private , protected.
There are three types of access modifier - 
1. public - Access Modifier
2. private - Access Modifier
3. protected - Access Modifier

'''
# Python does not enforce public, private, or protected access modifiers; they exist only as naming conventions followed by developers.


# public access modifier - (Anyone can access of this - )
class Person:
    def __init__(self):
        self.name = "Rohan Rathore"
a = Person()
print(a.name)

# private access modifier - (Outside of the class we can't access but we can access it)
class Person:
    def __init__(self):
        self.__name = "Rohan Rathore"   
a = Person()
# print(a.__name)   Can't be accessed directly.
print(a._Person__name)     # Can be accessed indirectly that's why we can say this is a name mangling in python.
print(a.__dir__())

