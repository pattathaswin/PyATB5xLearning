# program to find the max of 3 numbers
from selectors import SelectSelector

# i/p -> Interger
# o/p -> String/Integer

num1 = int(input("Please enter number1 \n"))
num2 = int(input("please enter number2 \n"))
num3 = int(input("Please enter number3 \n"))

if num1 > num2 and num1 > num3:
    print(f"the maximum number is {num1}")
elif num2 > num1 and num2 > num3:
    print(f"the maximum number is {num2}")
else:
    print(f"the maximum number is {num3}")
