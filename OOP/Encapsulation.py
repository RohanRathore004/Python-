"""
Encapsulation : Wrapping data (variables) and methods (functions) into a single unit (class) 
and protecting the data from direct access is called Encapsulation.

Note – Data is accessed only through class methods.

Example:
We cannot directly change money in an ATM machine; we must use buttons 
(deposit / withdraw) to access it safely.

"""
class BankAccount:
    def __init__(self,amount):
        self.__amount = amount
    
    def withdraw(self,amount):
        if amount <= self.__amount:
           self.__amount = self.__amount  - amount
           print("Withdrawan successfull")
           print(f"Banlance: {self.__amount}")
        else:
            print("Insufficient amount")

    def show_balance(self):
        print(self.__amount)


a = BankAccount(6000)
a.withdraw(400)
a.show_balance()
