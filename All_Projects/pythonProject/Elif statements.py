print("Welcome to the RollerCoster")

height = input("type your height in cm  ")

if int(height) >= 150:

  age = int(input("Enter Your Age! "))

  if  age <= 12:
      bill = 20
      print("child ticket fare $10")
  elif age >= 45 and age <= 55:

      print("your ride is free ")
  elif 12 < age < 18:
      bill = 15
      print("ticket fare is $15")

  else:
      bill = 10
      print("adult ticket fare $20  ")


  wants_photo = input("Do you want a photo?")
  if wants_photo == "Yes":
     final_bill = int(bill) + 3
     print(f"your final bill is {final_bill}")


else:
    print("Sorry you are not able to ride the Rollercoaster ")


#Complex BMI calculator

height = float(input("type your height in m:  "))
weight = float(input("type your weight in kg; "))
BMI = weight / height ** 2

if BMI < 18.5:
    print(f"your bmi is {BMI} you are Under weight")
elif 18.5 < BMI < 25:
    print(f"your bmi is {BMI} you are Normal Weight")
elif 25 < BMI < 30:
    print(f"your bmi is {BMI} you are Over weight ")
elif 30 < BMI < 35:
    print(f"your bmi is {BMI} you are Obese")
else:
    print(f"your bmi is {BMI} you are  Clinically Obese")



