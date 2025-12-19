"""
Abstraction : Hinding the implemention details of the class and showing the only essention details to user is called Abstraction:

Note - The internal working is hidden:
We go to ATM machine to take money but we don't need to know how the internally process is working in ATM machine.

Hinding the  unneccessary information and showing only the important information to user :

"""

class Car:
    def __init_(self):
        self.acc = False
        self.br= False
        self.cl = False
    
    def start(self):
        self.cl = True
        self.acc= True
        print("Car started...")
a = Car()
a.start()
