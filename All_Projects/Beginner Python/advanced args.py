def add(*args):
    print(type(args))
    print(args)
    num = 0
    for n in args:
        num += n
    print(num)

add(4, 5, 6, 8, 7, 9, 65, 54, 25, 14, 964, 789645, 564541485)

# kwargs
def calculate(n, **kwargs):
    # print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=78, multiply=5)


# creating kwargs in a class
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(model="GT-R")
print(my_car.make)
