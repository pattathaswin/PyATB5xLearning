

dict1 = {"a" : 1, "b" : 2, "c" : 5}
dict2 = {"c" : 3, "d" : 4}

missing_keys = set(dict1.keys()) - set(dict2.keys())
print(missing_keys)