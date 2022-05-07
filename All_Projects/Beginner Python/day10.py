#function with outputs
# first_num = int(input("Enter the number "))
# second_num = int(input("Enter the second number "))
# def calculation():
#     """ multiply the two numbers and gives the output"""
#     result = first_num * second_num
#     return result
# calculation()

# def format_name(f_name, l_name):
#    first_name = f_name.title()
#    # return f"{first_name} {second_name}"
# my_name = format_name("dEvEsh", "kUmAR")
# print(my_name)


def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return "True"
            else:
                return "False"
        else:
            return "True"
    else:
        return "False"


# def days_in_month(year, month):
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#
#     if is_leap(year) == "False":
#         return month_days[month - 1]
#     if is_leap(year) == "True":
#         if month == 2:
#             return 29
#         else:
#             return month_days[month - 1]
#
#
# # 🚨 Do NOT change any of the code below
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)
#
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
# def add(n1, n2):
#     return n1 + n2
#
# def subtract(n1, n2):
#     return n1 - n2
#
# def multiply(n1, n2):
#     return n1 * n2
#
# def divide(n1, n2):
#     return n1 / n2
#
# operation_dictionary = {"+": add,
# "-": subtract,
# "*": multiply,
# "/": divide
# }
# def calculator():
#
#     first_num = float(input("What's the first number "))
#
#     for operator in operation_dictionary:
#         print(operator)
#     should_continue = True
#     while should_continue:
#         operation = input("Which operation you want to run?  ")
#         second_num = float(input("What's the next number "))
#         calc = operation_dictionary[operation]
#         answer = calc(first_num, second_num)
#
#         print(f"{first_num} {operation} {second_num} = {answer}")
#
#         choice = input(f"Type 'y' to continue with with {answer}, or type 'n' to start a new calculation   ")
#
#         if choice == "y":
#            first_num = answer
#         else:
#             should_continue = False
#             calculator()
# calculator()

def a_function(a_parameter):
    a_variable = 15
    return a_parameter
a_function(10)
print(a_variable)






