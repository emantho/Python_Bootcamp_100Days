def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
                # print("Leap Year")
            else:
                return False
                # print("Not leap year")
        else:
            return True
            # print("Leap Year")
    else:
        return False
        # print(f"Not Leap Year")


def days_in_month(u_year, u_month):
    # leap_year february has 29 days
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(u_year):
        return month_days[u_month - 1] + 1
    else:
        return month_days[u_month - 1]


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month (in number): "))
days = days_in_month(year, month)
print(days)
