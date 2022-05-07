# import csv
import pandas
# # data = []
# # with open("weather_data.csv") as weather_data:
# #     for one_day in weather_data.readlines():
# #         my_day = one_day.strip()
# #         data.append(my_day)
# #
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         temperatures.append(int(row[1]))
# # print(temperatures)
#
data = pandas.read_csv("weather_data.csv")
# # print(data["temp"])
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# # my_temp = 0
# # for temp in temp_list:
# #     my_temp += temp
# # total_temp = len(temp_list)
# #
# # avg = my_temp / total_temp
# # print(round(avg, 2))
#
# print(data["temp"].mean())
#
# print(data["temp"].max())
#
# # we can also do like this
# print(data.day)
#
# # Get data in a row
print(data[data.day == "Monday"])
#
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# tempo = monday.temp
# f = (tempo * 9 / 5) + 32
# print(f)
#
# # how to create a dataframe from a scratch

num = 0
my_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrel = len(my_data[my_data["Primary Fur Color"] == "Gray"])
red_squirrel = len(my_data[my_data["Primary Fur Color"] == "Cinnamon"])
black_squirrel = len(my_data[my_data["Primary Fur Color"] == "Black"])

squirrel_dict = {
    "FurColor": ["Black", "Gray", "Red"],
    "Count": [black_squirrel, gray_squirrel, red_squirrel]
}

new_data = pandas.DataFrame(squirrel_dict)
new_data.to_csv("my_file.csv")










