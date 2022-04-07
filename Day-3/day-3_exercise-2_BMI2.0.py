# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
bmi = round(weight / height**2)
bold_start = "\033[1m"
bold_end = "\033[0m"

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are {bold_start}underweight.{bold_end}")
elif 18.5 <= bmi < 25:
    print(f"Your BMI is {bmi}, you have a {bold_start}normal weight.{bold_end}")
elif 25 <= bmi < 30:
    print(f"Your BMI is {bmi}, you are {bold_start}slightly overweight.{bold_end}")
elif 30 <= bmi < 35:
    print(f"Your BMI is {bmi}, you are {bold_start}Obese{bold_end}")
else:
    print(f"Your BMI is {bmi}, you are {bold_start}clinically obeses{bold_end}")
