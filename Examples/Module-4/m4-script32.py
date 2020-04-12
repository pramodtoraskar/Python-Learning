
# Program to demonstrate indexing in numpy

import numpy as np

# Slicing array
arr = np.array([[-1, 2, 0, 4],
                [4, -0.5, 6, 0],
                [2.6, 0, 7, 8],
                [3, -7, 4, 2.0]])


temp = arr[:2, ::2]
print("Array with first 2 rows and alternate columns(0 and 2):\n", temp)


# Integer array indexing example
temp = arr[[0, 1, 2, 3], [3, 2, 1, 0]]
print("\nElements at indices (0, 3), (1, 2), (2, 1),(3, 0):\n", temp)


# Boolean array indexing example
# cond is a boolean array
cond = arr > 0
temp = arr[cond]
print("\nElements greater than 0:\n", temp)


# ----------------------------------------------------------------------------------------------
# Program to demonstrate basic operations on single array
import numpy as np

np_arr = np.array([1, 2, 5, 3])

# Add 1 to every element
print("Adding 1 to every element:", np_arr + 1)

# Subtract 3 from each element
print("Subtracting 3 from each element:", np_arr - 3)

# Multiply each element by 10
print("Multiplying each element by 10:", np_arr * 10)

# Square each element
print("Squaring each element:", np_arr ** 2)

# modify existing array
np_arr *= 2
print("Doubled each element of original array:", np_arr)

# Transpose of array
new_np_arr = np.array([[1, 2, 3], [3, 4, 5], [9, 6, 0]])

print("\nOriginal array:\n", new_np_arr)
print("Transpose of array:\n", new_np_arr.T)


# ----------------------------------------------------------------------------------------------
# Unary operators
np_arr = np.array([[1, 5, 6],
                   [4, 7, 2],
                   [3, 1, 9]])

# Maximum element of array
print("Largest element is:", np_arr.max())
print("Row-wise maximum elements:", np_arr.max(axis=1))

# minimum element of array
print("Column-wise minimum elements:", np_arr.min(axis=0))

# sum of array elements
print("Sum of all array elements:", np_arr.sum())

# Cumulative sum along each row
print("Cumulative sum along each row:\n", np_arr.cumsum(axis=1))


# ----------------------------------------------------------------------------------------------
# Program to demonstrate binary operators in Numpy

np_arr_1 = np.array([[1, 2],
                     [3, 4]])
np_arr_2 = np.array([[4, 3],
                     [2, 1]])

# Add arrays
print("Array sum:\n", np_arr_1 + np_arr_2)

# Multiply arrays (Element-wise multiplication)
print("Array multiplication:\n", np_arr_1 * np_arr_2)

# Matrix multiplication
print("Matrix multiplication:\n", np_arr_1.dot(np_arr_2))


# ----------------------------------------------------------------------------------------------
# Program to demonstrate sorting in numpy

np_arr = np.array([[1, 4, 2],
                   [3, 4, 6],
                   [0, -1, 5]])

# Sorted array
print("Array elements in sorted order:\n", np.sort(np_arr, axis=None))

# Sort array row-wise
print("Row-wise sorted array:\n", np.sort(np_arr, axis=1))

# Specify sort algorithm
print("Column wise sort by applying merge-sort:\n", np.sort(np_arr, axis=0, kind='mergesort'))

# Example to show sorting of structured array set alias names for dtypes
dtypes = [('name', 'S10'), ('grad_year', int), ('cgpa', float)]

# Values to be put in array
values = [('Pravin', 2009, 8.5), ('Rayan', 2008, 8.7), ('Inder', 2008, 7.9), ('Vikram', 2009, 9.0)]

# Creating array
new_np_arr = np.array(values, dtype=dtypes)
print("\nArray sorted by names:\n", np.sort(new_np_arr, order='name'))

print("Array sorted by graduation year and then cgpa:\n", np.sort(new_np_arr, order=['grad_year', 'cgpa']))

# ----------------------------------------------------------------------------------------------
# Save numpy array as csv file

# Define data
np_data = np.asarray([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]])
# Save to csv file
np.savetxt('np_data.csv', np_data, delimiter=',')

# ----------------------------------------------------------------------------------------------
# Load numpy array from csv file

# Load array
np_data = np.loadtxt('np_data.csv', delimiter=',')
# Print the array
print(np_data)
