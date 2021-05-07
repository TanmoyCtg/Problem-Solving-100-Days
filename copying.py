# shallow copy and deep copy
import copy


org = 5
cpy = org

cpy = 6

print(cpy, org)

my_list = [0, 1, 2,4]
# shallow copy

copy_list = copy.copy(my_list)

copy_list[0] = -20
print("copy list",copy_list)
print("orginal list", my_list)

# deep copy
nested_List = [[1,2,3], ['joy',20,'A']]

cpy = copy.copy(nested_List)

cpy [0][1] = -10

print(cpy, nested_List)