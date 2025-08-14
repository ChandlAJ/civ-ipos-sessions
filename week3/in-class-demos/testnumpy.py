import numpy as np

two_dim_list =[[1,2,3],[4,5,6]]

numpy_array = np.array(two_dim_list)
a_list_again = numpy_array.tolist()

print(two_dim_list)
print(numpy_array)
print(a_list_again)

print(numpy_array[0][2])