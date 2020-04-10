
![](https://www.python.org/static/img/python-logo.png)
 
## Functions
#### [Syntax, Arguments, Keyword Arguments, Return Values, Function Parameters]

- A function is a set of statements that take inputs, do some specific computation and produces output. 
- The idea is to put some commonly or repeatedly done task together and make a function, 
- So that instead of writing the same code again and again for different inputs, 
- we can call the function.
- Python provides built-in functions like print(), etc. but we can also create your own functions. 
- These functions are called user-defined functions.

    ```python
       # A simple Python function to check whether x is even or odd
       def even_odd_fun(x):
          if x % 2 == 0:
             print("even")
          else:
             print("odd")

        # Call function
        even_odd_fun(2) 
        even_odd_fun(3) 
    ```
  
- Default arguments
    - A default argument is a parameter that assumes a default value if a value is not provided in the function call 
      for that argument.

    ```python
       # Program to demonstrate default arguments 
       def test_fun(x, y=50):
           print("x: ", x)
           print("y: ", y) 
       
       # Call test_fun() with only argument
       test_fun(10)
    ```

- Keyword arguments
    - The idea is to allow caller to specify argument name with values so that caller does not need to remember order of parameters.

    ```python
       # Program to demonstrate Keyword Arguments
       def student_info(first_name, last_name):
            print(first_name, last_name) 
 
       # Keyword arguments				 
       student_info(first_name ='Ankitkumar', lastname ='Rajput')	 
       student_info(last_name ='Inder', firstname ='Punj')
    ```

- Variable length arguments
    - We can have both normal and keyword variable number of arguments.
    ```python
       # Python program to illustrate *args for variable number of arguments
       def test_args_list_fun(*argv):
           for arg in argv:
               print(arg) 
       
       test_args_list_fun('Hello', 'Welcome', 'to', 'RedHat!') 
    ```

    ```python
       # Program to illustrate *kargs for variable number of keyword arguments 
       def test_args_dict_fun(**kwargs):
           for key, value in kwargs.items():
               print ("%s == %s" %(key, value)) 
 
       test_args_dict_fun(first ='Pramod', mid ='S', last='Toraskar')	 
    ```
    
- Anonymous functions
    - Anonymous function means that a function is without a name. 
    - As we already know that def keyword is used to define the normal functions and 
    - The lambda keyword is used to create anonymous functions
    
    ```python
      # Code to illustrate cube of a number using labmda function
      get_cube = lambda x: x*x*x 
      print(get_cube(7))
    ```

- Pass by reference vs value
    - All parameters (arguments) in the Python language are passed by reference
    - It means if you change what a parameter refers to within a function, the change also reflects back in the calling function
    
    ```python
        # Definition
        def change_param(list_obj):
           """This changes a passed list into this function"""
           list_obj.append([1,2,3,4])
           print("Values inside the function: ", list_obj)
           return
        
        # Call change_param function
        list_obj = [10,20,30]
        change_param(list_obj)
        print("Values outside the function: ", list_obj)
    ``` 

    - The reference is being overwritten inside the called function.
    ```python
        # Definition
        def change_param(list_obj):
           """This changes a passed list into this function"""
           list_obj = [1,2,3,4]
           print("Values inside the function: ", list_obj)
           return
        
        # Call change_param function
        list_obj = [10,20,30]
        change_param(list_obj)
        print("Values outside the function: ", list_obj)
    ```

- Return Values
    - The statement return [expression] exits a function
    
        ```python
        # Definition
        def get_num_sum( arg1, arg2 ):
           """Add both the parameters and return them."""
           num_total = arg1 + arg2
           print("Inside the function : ", num_total)
           return num_total
        
        # Now you can call sum function
        get_total = get_num_sum( 10, 20 )
        print("Outside the function : ", get_total)    
        ```
  [Example Script 25 - m3-script25.py](/Examples/Module-3/m3-script25.py)
#
[Main...](https://github.com/ptoraskar/Python-Learning/blob/master/README.md) | [Back...](/Module-3/1_python_standard_libraries.md) | [Next...](/Module-3/3_Variables.md)