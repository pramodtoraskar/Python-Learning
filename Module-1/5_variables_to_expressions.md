
![](https://www.python.org/static/img/python-logo.png)

 
## Values, Types, Variables
- Variables are nothing but reserved memory locations to store values.
- Based on the data type of a variable, the interpreter allocates memory
- Variables in Python are not “statically typed”. 
- A variable is created the moment we first assign a value to it.


### Values to Variables

- The operand to the left of the = operator is the name of the variable and 
  the operand to the right of the = operator is the value stored in the variable. <br/> 
  For example -      
    ```python
    
        # An integer assignment 
        age = 34					
            
        # A floating point 
        salary = 4560.8			
        
        # A string 
        name = "Pramod"			
            
        print(age) 
        print(salary) 
        print(name) 
    
    ```
    [Example Script 2: m1-script2.py](Examples/Module-1/m1-script2.py)
    
- Multiple Assignment

    ```python
      variable_1 = variable_2 = variable_3 = 1
    ```

- Standard Data Types

  - Numbers
  - String
  - List
  - Tuple
  - Dictionary

    ```python
    # Example of List variable and assignment
    list_1 = [ 'pqrst', 867 , 3.14, 'pune', 7.2 ]
    ```
    
    ```python
    # Example of Tuple variable and assignment
    tuple_1 = ('pqrst', 867 , 3.14, 'pune', 7.2)
    ```

    ```python
    # Example of Dictionary variable and assignment
    dict_1 = {'dept': 'sales', 'code': 6734, 'name': 'john'}
    ```
    
    [Example Script 3: m1-script3.py](Examples/Module-1/m1-script3.py)
 
- Type Conversion
 
     | Sr.No. | Function        |   Description                                                          |
     |--------|---------------- |------------------------------------------------------------------------|
     |  1     | int(x [,base])  | Converts x to an integer. base specifies the base if x is a string.    |
     |  2     | float(x)        | Converts x to a floating-point number.                                 |
     |  3     | str(x)          | Converts object x to a string representation.                          |
     |  4     | eval(str)       | Evaluates a string and returns an object.                              |
     |  5	  | tuple(s)        | Converts s to a tuple.                                                 |
     |  6     | list(s)         | Converts s to a list.                                                  |
     |  7     | set(s)          | Converts s to a set.                                                   |
     |  8     | dict(d)         | Creates a dictionary. d must be a sequence of (key,value) tuples.      |

 
## Operands and Expressions

- Operators are the main building block of any programming language.

    - Arithmetic operators
    
        ```python
            # Examples of Arithmetic Operator  
            num_1 = 9
            num_2 = 4
                
            # Addition of numbers  
            add_num = num_1 + num_2
        
            # Subtraction of numbers   
            sub_num = num_1 - num_2
        
            # Multiplication of number   
            mul_num = num_1 * num_2
        
            # Division(float) of number   
            div1_num = num_1 / num_2
        
            # Division(floor) of number   
            div2_num = num_1 // num_2
        
            # Modulo of both number  
            mod_num = num_1 % num_2  
                
            # print results  
            print(add_num)  
            print(sub_num)  
            print(mul_num)  
            print(div1_num)  
            print(div2_num)  
            print(mod_num)
        ```
    [Example Script 4: m1-script4.py](Examples/Module-1/m1-script4.py)

    - Relational Operators
    
        ```python
            # Examples of Relational Operators 
            num_1 = 13
            num_2 = 33
                
            # num_1 > num_2 is False 
            print(num_1 > num_2) 
                
            # num_1 < num_2 is True 
            print(num_1 < num_2) 
                
            # num_1 == num_2 is False 
            print(num_1 == num_2) 
                
            # num_1 != num_2 is True 
            print(num_1 != num_2) 
                
            # num_1 >= num_2 is False 
            print(num_1 >= num_2) 
                
            # num_1 <= num_2 is True 
            print(num_1 <= num_2) 

        ```
    [Example Script 5: m1-script5.py](Examples/Module-1/m1-script5.py)

    - Logical Operators
    
        ```python

            # Examples of Logical Operator  
            num_1 = True
            num_2 = False
                
            # Print num_1 and num_2 is False  
            print(num_1 and num_2)  
                
            # Print num_1 or num_2 is True  
            print(num_1 or num_2)  
                
            # Print not num_1 is False  
            print(not num_1)  
        ```
        
    [Example Script 6: m1-script6.py](Examples/Module-1/m1-script6.py)
 
    - Bitwise operators
    
        ```python
        
            # Examples of Bitwise operators  
            num_1 = 10
            num_2 = 4
                
            # Print bitwise AND operation    
            print(num_1 & num_2)  
                
            # Print bitwise OR operation  
            print(num_1 | num_2)  
                
            # Print bitwise NOT operation   
            print(~num_1)  
                
            # print bitwise XOR operation   
            print(num_1 ^ num_2)  
                
            # print bitwise right shift operation   
            print(num_1 >> num_2)  
                
            # print bitwise left shift operation   
            print(num_1 << num_2) 

        ```  

#
[Main...](https://github.com/ptoraskar/Python-Learning/blob/master/README.md) | [Back...](/Module-1/4_setup_python_environment.md) | [Next...](/Module-1/6_loops_and_conditions.md)


