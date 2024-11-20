# type of User defined fucntions

#Simple

def greet():
    print ("Hello World")

#With Argument
greet()

def hello(name):
    print ("hello, ", name)

hello ("pramod")

#with default Argument
def say_hello_default_arg (name="Aswin"):
    print("Hello, ",  name.upper())

say_hello_default_arg ()
say_hello_default_arg ("Kumar")

#with return

def sum_of_two_numbers (a, b):
    return a + b

result = sum_of_two_numbers (40, 50)
print (result)


def sum_of_two_numbers_with_default (a = 500, b = 300):
    return a + b

result = sum_of_two_numbers_with_default (100, 200)
print (result)
result = sum_of_two_numbers_with_default ()
print (result)

