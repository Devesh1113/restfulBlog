# Class Inheritance

class Animal:
    def __init__(self):
        self.eyes = 2
        self.legs = 4

    def breathe(self):
        print("We can breathe only in air")


class Dog(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("Breathes fast after running")

    def bark(self):
        print("Shout on strangers")


my_dog = Dog()
my_dog.bark()
my_dog.breathe()
print(my_dog.eyes)

# slicing a list
piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
print(piano_keys[1:6])

name_list = ["d", "e", "v", "e", "s", "h"]
print(name_list[6:0:-1])

