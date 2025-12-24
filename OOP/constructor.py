# A constructor in Python is used to initialize object variables at the time of object creation; it can be parameterized or default.


class First:
    def __init__(self,name,city):   # This is parameterised constructor - 
        self.name = name
        self.city = city
    def info(self):
        print(f"Your name is {self.name} and your city is {self.city}")
a = First("Rohan Rathore","Indore")
b = First("Vishal Malviya","Dewas")
a.info()
b.info()


"""
There are two types of constructors - 
1. Parameterised constructor - (Pass the parameter)
2. Default constructor -     ( Default value which takes only self )

"""