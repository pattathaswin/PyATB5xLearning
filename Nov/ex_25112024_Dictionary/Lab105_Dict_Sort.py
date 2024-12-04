#Sort the values in dictionary in ascending or descending order

my_dict = {"a" : 3, "b" : 1, "d" :5, "c" : 2}

my_dict_sorted = dict(sorted(my_dict.items(), key = lambda item : item[1]))


print(my_dict_sorted)

