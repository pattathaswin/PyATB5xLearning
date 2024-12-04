# write a program to calculate the number of characters in the string

#string = input("enter the string")
string = "automation"

char_count =  {}

for char in string:
    char_count[char] = char_count.get(char, 0) + 1

print (char_count)


