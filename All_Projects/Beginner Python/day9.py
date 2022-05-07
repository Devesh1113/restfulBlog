#Dictionary
programming_dictionaries = {"print": "used to the information typed inside the print command",
 "if": "a function in programming used to do logical opeartions",
 "string": "collection of a number of characters of anything"}

print(programming_dictionaries["print"])
programming_dictionaries["loop"] = "The action of doing something again and again"
print(programming_dictionaries)


for key in programming_dictionaries:
 print(key)
 print(programming_dictionaries[key])

student_scores = {
 "harry": 81,
 "Ron": 78,
 "Hermione": 99,
 "devesh": 67
}

student_grades = {}
for scores in student_scores:
 if student_scores[scores] > 90:
    student_scores[scores] = "Outstanding"
 elif 90 > student_scores[scores] >= 81:
    student_scores[scores] = "Exceeds Expectations"
 elif 80 > student_scores[scores] >= 71:
    student_scores[scores] = "Acceptable"
 elif student_scores[scores] <= 70:
    student_scores[scores] = "Fails"

 student_grades = student_scores
print(student_grades)

travel_log = {
    "France":[{"Paris": 2}, {"little": 1} , {"Dijon": 4}],
    "Delhi": {"Travelled_in_metro": 5, }}
print(travel_log)

#adding a list ina dictionary
my_list = [
    {
     "Favorite_movies": ["wolf_of_wall_street", "Titanic", "interstellar"]
    },
    {
     "Favorite_series": ["peaky"]
    },
]
print(my_list)

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

first_num = int(input("Type the first number  "))
second_num = int(input("Type the second number  "))

product = first_num * second_num
if product < 1000:
    print(product)
elif product > 1000:
    sum = first_num + second_num
    print(sum)






























