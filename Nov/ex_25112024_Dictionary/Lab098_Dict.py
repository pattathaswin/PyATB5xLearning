from Nov.ex_25112024_Dictionary.Lab096_Dict import my_dict

student_infor = {
    "name" : " aswin",
    #"age" : 65,
    "age" : 67,
    "address" : "KA"
}

print(student_infor["name"])
print(student_infor["age"])
print(student_infor["address"])
student_infor["age"] = 100
print(student_infor["age"])

print ("age" in my_dict)
