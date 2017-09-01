import numpy as np

array = np.zeros(10)  # new array with 10 zeros
array[3] = 5  # Assign to an element
array[5:8] += 2  # In-place add to several elements
print(array[5])  # Print an element
array2 = 2 * array  # Multiply by 2, creating new array
array *= 2  # Multiply all elements in-place

array2D = np.random.rand(4, 8)  # 4 x 8 random numbers
print(array2D)  # Print whole array
print(array2D[:, 0])  # Print first row
print(array2D[:, 7])  # Print last row
print(array2D[0, :])  # Print first column
