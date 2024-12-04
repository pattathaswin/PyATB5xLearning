#remove duplicates

my_list = [1,2,2,3,4,5,5,6,7]

new_list = set(my_list)

new_list1 = list(new_list)

print(new_list1)

# Alternate Item

# new_uniq_list = []
#
# for item in my_list:
#     if item not in new_uniq_list:
#         new_uniq_list.append(item)
#
# print(new_uniq_list)