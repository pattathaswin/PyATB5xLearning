my_list = [1,2,3, 9, 10, 6, 7]

#indexing

print ("element at the index 0 - ", my_list[0])
print ("element at the index 1 - ", my_list[1])
print ("element at the index 2 - ", my_list[2])


#insert()

my_list.insert(1, "Aswin")
print (my_list)
print(len(my_list))


my_list[1] = "Amit"
print (my_list)

#remove()
my_list.remove("Amit")
print(my_list)

#copy()
copy_my_list = my_list.copy()
print(my_list)
print(copy_my_list)

#sort()

my_list.sort()
print(my_list)
