# Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides,
# determine if the triangle is equilateral (all sides are equal),
# isosceles (exactly two sides are equal),
# or scalene (no sides are equal). Use an if-else statement to classify the triangle.

# input 3 sides - int
# out string - Iso, eq, scelene

side1 = int(input("Enter the value of Side 1 \n "))
side2 = int(input("enter the value of side 2 \n"))
side3 = int(input("Enter the value of side 3 \n"))

if side1 == side2 and side1 == side3:
    print("The triage is Equivalent Triangle")
elif side1 == side2 and side1 != side3:
    print("The Triangle is Isosceles Triangle")
elif side1 == side3 and side1 != side2:
    print("The Triangle is Isosceles Triangle")
elif side2 == side3 and side1 != side2:
    print("The Triangle is Isosceles Triangle")
else:
    print("The triangle is Scalene triangle")
