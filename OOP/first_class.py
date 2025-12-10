# class - class is just named group properties of function:
class Person:
    name = input("Enter the your name here: ")
    college = input("Enter the your college name here: ")
    
    # Create a function for printing the information about the Person.
    def info(self):
        print(f"Your name is {self.name} and your college name is {self.college}")
first = Person()
first.name = ("Rohan Rathore")
first.college = ("Sage university Indore")
first.info()

second = Person()
second.info()

# Note - Class name always should be starts with Capital letters.
