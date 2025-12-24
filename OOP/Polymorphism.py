# Polymorphism allows the same method name to perform different actions based on the object.

class Animal:
    def speak(self):
        print("Animal speak")

class Dog:
    def speak(self):
        print("Dog Barks")

a = Animal()
a.speak()
b = Dog()
b.speak()
