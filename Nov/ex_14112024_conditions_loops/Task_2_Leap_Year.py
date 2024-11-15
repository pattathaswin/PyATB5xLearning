# Leap day occurs in each year that is a multiple of 4,
# except for years evenly divisible by 100 but not by 400.


year = int(input("Please enter the year \n"))

firstvalue = year % 4
secondvalue = year % 100
thirdvalue = year % 400
if (firstvalue == 0 and secondvalue != 0) or thirdvalue == 0:
    print(f"The entered year {year} is a leap year")
else:
    print(f"The entered year {year} is not a leap year")
