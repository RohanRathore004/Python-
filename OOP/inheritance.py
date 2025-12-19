"""
Inheritance : Using the one class property into the another class is called inheritance:
There are three types of inheritance:
1.single inheritance
2.Multi level inheritance
3.Multiple inheritance

"""
# parent class
class Kripal:
    def main(self):
        print("This is base class:")

# child class:
class Rohan(Kripal):
    def lower_main(self):
        print("This is first child class:")

# second child class:
class RR(Rohan):
    def double_lower_main(self):
        print("This is second child class")

a = RR()
a.main()
a.lower_main()
a.double_lower_main()
