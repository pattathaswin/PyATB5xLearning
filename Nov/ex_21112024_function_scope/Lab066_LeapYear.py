def check_leap_year(Year):
    if (year % 4 == 0 and year % 100 != 0) or  (year % 4  == 400):
        return True
    else:
        return False

year = 2024

if check_leap_year(year):
    print("Yes")
else:
    Print ("No")