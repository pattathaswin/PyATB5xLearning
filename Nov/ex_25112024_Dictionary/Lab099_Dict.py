dict ()

# get()
# keys()
# values()
# items()
# updated()
# pop()
# clear()

student_infor = {
    "name" : " aswin",
    #"age" : 65,
    "age" : 67,
    "address" : "KA"
}

print(student_infor["name"])

student_infor2 = dict(name="aswin", age = 89, address = "HY")


student_infor1 = {
    "name" : " aswin",
    #"age" : 65,
    "age" : 67,
    "address" : {
        "home_address" : "ND",
        "office_address" : "KA"
    }

}
