input_string = "Hello, World!"
#a,e,i,o,u

vowels = "aeiou"

vowels_count = 0
result = {}

for char in input_string:
    if char in vowels:
        vowels_count = vowels_count + 1

print (vowels_count)