
# Program to demonstrate basic array characteristics
import numpy as np

# Creating array object
arr = np.array([[1, 2, 3],
                [4, 2, 5]])

# Printing type of arr object
print("Array is of type: ", type(arr))

# Printing array dimensions (axes)
print("No. of dimensions: ", arr.ndim)

# Printing shape of array
print("Shape of array: ", arr.shape)

# Printing size (total number of elements) of array
print("Size of array: ", arr.size)

# Printing type of elements in array
print("Array stores elements of type: ", arr.dtype)


# Program to demonstrate array creation techniques
# -----------------------------------------------------------------

# Creating array from list with type float
np_aar_1 = np.array([[1, 2, 4], [5, 8, 7]], dtype='float')
print("Array created using passed list:\n", np_aar_1)

# Creating array from tuple
np_aar_2 = np.array((1, 3, 2))
print("\nArray created using passed tuple:\n", np_aar_1)

# Creating a 3X4 array with all zeros
np_aar_3 = np.zeros((3, 4))
print("\nAn array initialized with all zeros:\n", np_aar_3)

# Create a constant value array of complex type
np_aar_4 = np.full((3, 3), 6, dtype='complex')
print("\nAn array initialized with all 6s. Array type is complex:\n", np_aar_1)

# Create an array with random values
np_aar_5 = np.random.random((2, 2))
print("\nA random array:\n", np_aar_5)

# Create a sequence of integers from 0 to 30 with steps of 5
np_aar_6 = np.arange(0, 30, 5)
print("\nA sequential array with steps of 5:\n", np_aar_6)

# Create a sequence of 10 values in range 0 to 5
np_aar_7 = np.linspace(0, 5, 10)
print("\nA sequential array with 10 values between 0 and 5:\n", np_aar_7)

# Reshaping 3X4 array to 2X2X3 array
np_aar_8 = np.array([[1, 2, 3, 4],
                     [5, 2, 4, 2],
                     [1, 2, 0, 1]])

new_np_arr = np_aar_8.reshape(2, 2, 3)

print("\nOriginal array:\n", np_aar_8)
print("Reshaped array:\n", new_np_arr)

# Flatten array
np_arr = np.array([[1, 2, 3], [4, 5, 6]])
fl_np_arr = np_arr.flatten()

print("\nOriginal array:\n", np_arr)
print("Fattened array:\n", fl_np_arr)

