# import time
#
#
# def addition(n1, n2):
#     return n1 + n2
#
#
# def subtraction(n1, n2):
#     return n1 - n2
#
#
# def multiply(n1, n2):
#     return n1 * n2
#
#
# def division(n1, n2):
#     return n1 / n2
#
#
# def calculate(calc, n1, n2):
#     return calc(n1, n2)
#
#
# # python function can be passed as arguments as below, they are called first class objects
# result = calculate(multiply, 2, 3)
# print(result)
#
#
# # Neste Function
#
# # def outer_function():
# #     print("I'm outer")
# #
# #     def inner_function():
# #         print("I'm inner")
# #     inner_function()
# #
# #
# # outer_function()
#
# # Functions can be returned from other functions
#
#
# def outer_function():
#     print("I'm outer")
#
#     def nested_function():
#         print("I'm inner")
#
#     return nested_function
#
#
# inner_function = outer_function()
#
# inner_function()
#
#
# # Python Decorators
#
#
# def decorator_function(func):
#     def wrapper_function():
#         time.sleep(2)
#         func()
#
#     return wrapper_function
#
#
# # First Method
# def say_hello():
#     print("Hello")
#
#
# my_wrap = decorator_function(say_hello)
# my_wrap()
#
#
# # Second Method(Preferable)
# @decorator_function
# def say_hello():
#     print("Hello")
#
#
# say_hello()


# Advanced Decorators
class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])

    return wrapper


@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")


new_user = User("Devesh")
# print(new_user.name)
new_user.is_logged_in = True
create_blog_post(new_user)


# Advanced Decorators Coding Exercise

def logging_decorator(function):
    def wrapper(*args):
        text = function(args[0], args[1], args[2])
        print(f"You called {function.__name__}{args[0], args[1], args[2]}")
        print(f"It returned {text}")

    return wrapper


@logging_decorator
def addition(*args):
    add = 0
    for arg in args:
        add += arg
    print(add)


addition(1, 2, 3)
