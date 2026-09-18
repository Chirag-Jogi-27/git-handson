class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):  # Dog inherits from Animal
    def speak(self):
        print(f"{self.name} barks.")

class Cat(Animal):  # Cat inherits from Animal
    def speak(self):
        print(f"{self.name} meows.")

# Usage
d = Dog("Rex")
c = Cat("Whiskers")

d.speak()  # Rex barks.
c.speak()  
