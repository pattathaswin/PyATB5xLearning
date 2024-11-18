# write a program to ask user which browser he wants to run the program

browser_name = input("please enter the browser name \n")
match browser_name:
    case "firefox":
        print ("Starting firefox")
    case "chrome":
        print ("Starting chrome")
    case _:
        print("browser not supported")


