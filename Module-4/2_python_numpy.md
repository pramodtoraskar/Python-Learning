
![](https://www.python.org/static/img/python-logo.png)

## Numpy
 - NumPy is a general-purpose array-processing package
 - Provides a high-performance multidimensional array object, and tools for working with these arrays.
 - It is the fundamental package for scientific computing with Python
 - Features
    - A powerful N-dimensional array object
    - Sophisticated (broadcasting) functions
    - Tools for integrating C/C++ and Fortran code
    - Useful linear algebra, Fourier transform, and random number capabilities
     
 - Installation
    ```bash
       pip install numpy
    ```
    Note: for windows we need to download from prebuild source: https://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy     

 - Create arrays using NumPy
    - NumPy’s main object is the **homogeneous multidimensional** array
    - It is a table of elements (usually numbers), all of the same type, indexed by a tuple of positive integers.
    - In NumPy dimensions are called **axes**. The number of axes is **rank**.
    - NumPy’s array class is called **ndarray**. It is also known by the alias array. 
    
    ```python
        """
        [[ 1, 2, 3],
         [ 4, 2, 5]]
        
        Here,
           rank = 2 (as it is 2-dimensional or it has 2 axes)
           first dimension(axis) length = 2, 
           second dimension has length = 3
           overall shape can be expressed as: (2, 3)
        """
        # Program to demonstrate basic array characteristics 
        import numpy as np 
        
        # Creating array object 
        arr = np.array( [[ 1, 2, 3], 
                        [ 4, 2, 5]]) 
        
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
    
    ```
    - Type of array can be explicitly defined while creating array
    
    ```python
        # Program to demonstrate array creation techniques 
        import numpy as np 
        
        # Creating array from list with type float 
        np_aar_1 = np.array([[1, 2, 4], [5, 8, 7]], dtype = 'float') 
        print ("Array created using passed list:\n", np_aar_1) 
        
        # Creating array from tuple 
        np_aar_2 = np.array((1 , 3, 2)) 
        print ("\nArray created using passed tuple:\n", np_aar_1) 
        
        # Creating a 3X4 array with all zeros 
        np_aar_3 = np.zeros((3, 4)) 
        print ("\nAn array initialized with all zeros:\n", np_aar_3) 
        
        # Create a constant value array of complex type 
        np_aar_4 = np.full((3, 3), 6, dtype = 'complex') 
        print ("\nAn array initialized with all 6s. Array type is complex:\n", np_aar_1) 
        
        # Create an array with random values 
        np_aar_5 = np.random.random((2, 2)) 
        print ("\nA random array:\n", np_aar_5) 
        
        # Create a sequence of integers from 0 to 30 with steps of 5 
        np_aar_6 = np.arange(0, 30, 5) 
        print ("\nA sequential array with steps of 5:\n", np_aar_6) 
        
        # Create a sequence of 10 values in range 0 to 5 
        np_aar_7 = np.linspace(0, 5, 10) 
        print ("\nA sequential array with 10 values between 0 and 5:\n", np_aar_7) 
        
        # Reshaping 3X4 array to 2X2X3 array 
        np_aar_8 = np.array([[1, 2, 3, 4],
                             [5, 2, 4, 2], 
                             [1, 2, 0, 1]]) 
        
        new_np_arr = np_aar_8.reshape(2, 2, 3) 
        
        print ("\nOriginal array:\n", np_aar_8) 
        print ("Reshaped array:\n", new_np_arr) 
        
        # Flatten array 
        np_arr = np.array([[1, 2, 3], [4, 5, 6]]) 
        fl_np_arr = np_arr.flatten() 
        
        print ("\nOriginal array:\n", np_arr) 
        print ("Fattened array:\n", fl_np_arr) 
    ```
    [Example Script 31 - m2-script31.py](/Examples/Module-4/m4-script31.py) 
  
 - Indexing slicing and iterating
    - NumPy offers many ways to do array indexing.
    - Knowing the basics of array indexing is important for analysing and manipulating the array object.
    
    - Slicing
        - Like lists in python, NumPy arrays can be sliced
        - As arrays can be multidimensional, you need to specify a slice for each dimension of the array
    - Integer array indexing
        - lists are passed for indexing for each dimension. 
        - One to one mapping of corresponding elements is done to construct a new arbitrary array.
    - Boolean array indexing
        - To pick elements from array which satisfy some condition
    ```python
       # Slicing array
       arr = np.array([[-1, 2, 0, 4],
                       [4, -0.5, 6, 0], 
                       [2.6, 0, 7, 8], 
                       [3, -7, 4, 2.0]])     
       temp = arr[:2, ::2] 
       print ("Array with first 2 rows and alternate columns(0 and 2):\n", temp) 
       # Integer array indexing example 
       temp = arr[[0, 1, 2, 3], [3, 2, 1, 0]] 
       print ("\nElements at indices (0, 3), (1, 2), (2, 1),(3, 0):\n", temp) 
       # boolean array indexing example 
       cond = arr > 0 # cond is a boolean array 
       temp = arr[cond] 
       print ("\nElements greater than 0:\n", temp) 
    ```
    [Example Script 32 - m2-script32.py](/Examples/Module-4/m4-script32.py)
 - Basic operations
    - Operations on single array
        - We can use overloaded arithmetic operators to do element-wise operation on array to create a new array. 
        - In case of +=, -=, *= operators, the exsisting array is modified.
      ```python
        # Program to demonstrate basic operations on single array 
        import numpy as np
        
        np_arr = np.array([1, 2, 5, 3]) 
        
        # Add 1 to every element 
        print("Adding 1 to every element:", np_arr+1) 
        
        # Subtract 3 from each element 
        print("Subtracting 3 from each element:", np_arr-3) 
        
        # Multiply each element by 10 
        print("Multiplying each element by 10:", np_arr*10) 
        
        # Square each element 
        print("Squaring each element:", np_arr**2) 
        
        # modify existing array 
        np_arr *= 2
        print("Doubled each element of original array:", np_arr) 
        
        # Transpose of array 
        new_np_arr = np.array([[1, 2, 3], [3, 4, 5], [9, 6, 0]]) 
        
        print("\nOriginal array:\n", new_np_arr) 
        print("Transpose of array:\n", new_np_arr.T) 
      ```
    [Example Script 32 - m2-script32.py](/Examples/Module-4/m4-script32.py)
    - Unary operators
        - Many unary operations are provided as a method of ndarray class. 
        - Includes sum, min, max, etc. 
        - These functions can also be applied row-wise or column-wise by setting an axis parameter.
        ```python
        # Program to demonstrate unary operators in numpy 
        import numpy as np 
        
        np_arr = np.array([[1, 5, 6], 
                           [4, 7, 2], 
                           [3, 1, 9]]) 
        
        # Maximum element of array 
        print("Largest element is:", np_arr.max()) 
        print("Row-wise maximum elements:", np_arr.max(axis = 1)) 
        
        # minimum element of array 
        print ("Column-wise minimum elements:", np_arr.min(axis = 0)) 
        
        # sum of array elements 
        print ("Sum of all array elements:", np_arr.sum()) 
        
        # Cumulative sum along each row 
        print ("Cumulative sum along each row:\n", np_arr.cumsum(axis = 1))
        ```
    [Example Script 32 - m2-script32.py](/Examples/Module-4/m4-script32.py)
    - Binary operators
        - These operations apply on array element-wise and a **new array** is created. 
        - You can use all basic arithmetic operators like +, -, /, , etc. 
        - In case of +=, -=, = operators, the existing array is modified.
        ```python
        # Program to demonstrate binary operators in Numpy 
        import numpy as np 
        
        np_arr_1 = np.array([[1, 2], 
                             [3, 4]]) 
        np_arr_2 = np.array([[4, 3], 
                             [2, 1]]) 
        
        # Add arrays 
        print ("Array sum:\n", np_arr_1 + np_arr_2) 
        
        # Multiply arrays (Element-wise multiplication) 
        print ("Array multiplication:\n", np_arr_1*np_arr_2) 
        
        # Matrix multiplication 
        print ("Matrix multiplication:\n", np_arr_1.dot(np_arr_2)) 
        ```
    [Example Script 32 - m2-script32.py](/Examples/Module-4/m4-script32.py)        
    - Sorting array
        - There is a simple np.sort method for sorting NumPy arrays
        ```python
        # Program to demonstrate sorting in numpy 
        import numpy as np 
        
        np_arr = np.array([[1, 4, 2], 
                           [3, 4, 6], 
                           [0, -1, 5]]) 
        
        # Sorted array 
        print("Array elements in sorted order:\n", np.sort(np_arr, axis = None)) 
        
        # Sort array row-wise 
        print ("Row-wise sorted array:\n", np.sort(np_arr, axis = 1)) 
        
        # Specify sort algorithm 
        print ("Column wise sort by applying merge-sort:\n", np.sort(np_arr, axis = 0, kind = 'mergesort')) 
        
        # Example to show sorting of structured array set alias names for dtypes 
        dtypes = [('name', 'S10'), ('grad_year', int), ('cgpa', float)] 
        
        # Values to be put in array 
        values = [('Hrithik', 2009, 8.5), ('Ajay', 2008, 8.7), ('Pankaj', 2008, 7.9), ('Aakash', 2009, 9.0)] 
                    
        # Creating array 
        new_np_arr = np.array(values, dtype = dtypes) 
        print ("\nArray sorted by names:\n", np.sort(new_np_arr, order = 'name')) 
                    
        print ("Array sorted by grauation year and then cgpa:\n", np.sort(new_np_arr, order = ['grad_year', 'cgpa'])) 
        ```        
    [Example Script 32 - m2-script32.py](/Examples/Module-4/m4-script32.py)           
 - Read & write data from text/CSV files into arrays and vice-versa
    - Writing Numpy array to CSV file
        - We can store NumPy array to CSV format using **savetxt()**.
        ```python
        # Save numpy array as csv file
        from numpy import asarray
        from numpy import savetxt
        # Define data
        np_data = asarray([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]])
        # Save to csv file
        savetxt('np_data.csv', np_data, delimiter=',')
        ```
    - Reading Numpy array from CSV file
        - We can load data as a NumPy array using the **loadtext()** function.
        - Specify the filename and the same comma delimiter.
        ```python
        # Load numpy array from csv file
        from numpy import loadtxt
        
        # Load array
        np_data = loadtxt('np_data.csv', delimiter=',')
        # Print the array
        print(np_data)
        ```
#       
[Main...](https://github.com/ptoraskar/Python-Learning/blob/master/README.md) | [Back...](/Module-4/1_python_for_da_ds.md) | [Next...](/Module-4/3_python_pandas.md)