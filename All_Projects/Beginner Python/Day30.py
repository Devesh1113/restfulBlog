try:
    my_list = [1, 2, 3, 4, 5]
    output = my_list[1]
except IndexError as error_message:
    print(f"{error_message}")
else:
    if output == 3:
        print("Nice")
    else:
        print("Damn")
finally:
    print("My name is Devesh")

# raise KeyError("My Error")







