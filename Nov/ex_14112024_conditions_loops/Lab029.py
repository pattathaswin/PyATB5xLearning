#Write a program to take a user to the club
#Let him know if he can go to the club if his age is > 21


# logic building formula

#Step 1
#user input = Age = integer
#o/p -> String - user can go or not

# step 2
#rough logic

#if age>21, he can go
#if age<21, he cannot go

#step 3 - write the logic
user_age  = int(input("Please enter your age: "))

if user_age > 21:
    print(f"Yes, you are eligible to go to the club as your age is {user_age}")
else:
    print(f"Unfortunately, you are not eligible to enter the club as your age is {user_age}")

print ("------------------------------------")

#step 4  - Check the edge cases
# -ve values can be handled?
#big number can be handled?

#step 5 - optimize the code
