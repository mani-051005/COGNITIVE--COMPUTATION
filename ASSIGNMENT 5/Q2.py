import numpy as np
import matplotlib.pyplot as plt

# Q.2 (a) For the array: array = np.array([10, 52, 62, 16, 16, 54, 453]), find
array = np.array([10, 52, 62, 16, 16, 54, 453])

# i. Sorted array
sorted_array = np.sort(array)
print("Sorted array:", sorted_array)

# ii. Indices of sorted array
sorted_indices = np.argsort(array)
print("Indices of sorted array:", sorted_indices)

# iii. 4 smallest elements
smallest_elements = np.partition(array, 4)[:4]
print("4 smallest elements:", smallest_elements)

# iv. 5 largest elements
largest_elements = np.partition(array, -5)[-5:]
print("5 largest elements:", largest_elements)

import numpy as np
import matplotlib.pyplot as plt

# Q.2 (b) For the array: array = np.array([1.0, 1.2, 2.2, 2.0, 3.0, 2.0]), find
array = np.array([1.0, 1.2, 2.2, 2.0, 3.0, 2.0])

# i. Integer elements only
integer_elements = array[array == array.astype(int)]
print("Integer elements only:", integer_elements)

# ii. Float elements only
float_elements = array[array != array.astype(int)]
print("Float elements only:", float_elements)
