import pandas
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [number ** 2 for number in numbers]
# print(squared_numbers)
#
# result = [number for number in numbers if number % 2 == 0]
# print(result)
#
# list1 = []
# with open("file1") as file1:
#     for line in file1.readlines():
#         new_num = line.strip()
#         list1.append(new_num)
# print(list1)
#
# list2 = []
# with open("file2") as file2:
#     for line in file2.readlines():
#         new_num = line.strip()
#         list2.append(new_num)
# print(list2)
#
# result = [int(num) for num in list1 if num in list2]
# print(result)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

split_sentence = sentence.split(" ")
dict = {word: len(word) for word in split_sentence}
print(dict)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

fahrenheit_dictionary = {day: (temp * 9 / 5) + 32 for (day, temp) in weather_c.items()}
print(fahrenheit_dictionary)

student_dict = {
    "Students": ['Devesh', 'ankit', 'prince'],
    "Scores": [79, 76, 89]

}

weather_data_frame = pandas.DataFrame(student_dict)
# Looping through a DataFrame
for (index, row) in weather_data_frame.iterrows():
    print(row.Students)
    print(row.Scores)
    if row.Students == "Devesh":
        print(row.Scores)


# Project

