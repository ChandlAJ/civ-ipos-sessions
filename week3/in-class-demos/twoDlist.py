#
# var1 = 1
# var2 = 'string'
#
# var_list = [1, 2, 3]
#
# two_dim_list = [[1,2],
#                 [3,4]]
#
# print(two_dim_list[1][1])
#
# for item in two_dim_list:
#     for element in item:
#         print(element)
#
# rows, columns = 5,5
# new_two_dim_list = []
#
# for i in range(rows):
#     row = []
#     for j in range(columns):
#         row.append((i+1)*(j+1))
#     new_two_dim_list.append(row)
#
# print(new_two_dim_list)

height, width = 3, 3
image_structure = []

for i in range(height):
    row = []
    for j in range(width):
        point = {"R": 2, "G": 3, "B":5}
        row.append(point)
    image_structure.append(row)

print(image_structure)

def modify_list(list_):
    list_.append("new")
    list_ = ["completely", "new"]

items = ["original"]
modify_list(items)
print(items)

