def Classify_triangle(a, b, c):
    if a > 0 and b > 0 and c > 0:
        if a + b > c and b + c > a and a+c > b:
            if a == b == c:
                return "Equilateral"
            elif a == b or b == c or a == c:
                return "Isosceles"
            else:
                return "Scalene"
        else:
            print("not a triangle")
    else:
        print ("Not a valid length")

side1 = float(input ("Enter the first side \n"))
side2 = float(input ("Enter the second side \n"))
side3 = float(input ("Enter the third side \n"))

result = Classify_triangle(side1, side2, side3)
print (f"The triage is classified as: {result}")