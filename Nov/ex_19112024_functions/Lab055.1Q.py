#create a program to find the sum of 3 numbers from user input
#if user doesn't enter any number, then take the default values as 100,200, 300


num1 = int(input ("enter the 1st number \n"))
num2 = int(input ("enter the 1st number \n"))
num3 = int(input ("enter the 1st number \n"))


def sum_of_three_numbers(num1 = 100, num2 = 200, num3 = 300):
    return num1+num2+num3

result = sum_of_three_numbers (num1, num2, num3)
print (result)