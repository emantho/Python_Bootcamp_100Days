from os import system

system("clear")

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
age = int(age)

year_in_days = 365
year_in_weeks = 52.1429
year_in_months = 12

age_in_days = year_in_days * age
age_in_weeks = year_in_weeks * age
age_in_months = year_in_months * age

left_in_days = 90 * year_in_days - age_in_days
left_in_weeks = 90 * year_in_weeks - age_in_weeks
left_in_months = 90 * year_in_months - age_in_months

print(
    f"You have {left_in_days} days, {left_in_weeks:.0f} weeks, and {left_in_months} months left."
)

#  ----- OTHER SOLUTION ------

# years_remaining = 90 - int(age)

# left_in_days = year_in_days * years_remaining
# left_in_weeks = year_in_weeks * years_remaining
# left_in_months = year_in_months * years_remaining

# print(f"You have {left_in_days} days, {left_in_weeks:.0f} weeks, and {left_in_months} months left.")
