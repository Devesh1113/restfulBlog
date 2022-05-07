# making an object
# from turtle import Turtle, Screen
# # we Know object = Class() and here we imported the module and now we will make an object
# tinny = Turtle()
# # to run methods attached to an object: object.method()
# tinny.shape("turtle")
# tinny.color("darkblue")
# tinny.circle(100)
#
# my_screen = Screen()
#
# # to run attached attached to an object: object.attribute
# print(my_screen.canvheight)
# my_screen.exitonclick()

# from turtle import *
# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()

from prettytable import PrettyTable

my_table = PrettyTable()
my_table.add_column("Names", ["Devesh", "Ankit", "prince", "aakash", "Naveen", "harshit", "Virat", "dhoni"])
my_table.add_column("Numbers", [13, 45, 65, 78, 89, 90, 12, 34])

print(my_table)

# Coffee making Machine through oop




















