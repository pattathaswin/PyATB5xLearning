# Before or after running the code, we can do some action

def add_extra_security(func):
    def wrapper():
        print("Before Driving Scooty, Please wear a healmet")
        func()
        print ("Driving is completed")
    return wrapper()

@add_extra_security
def drive_ola():
    print ("I want to drive ola")

@add_extra_security
def drive_scooty():
    print ("Normal function!!")
    print ("I am driving Scooty")