
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
    [Example Script 2: m1-script2.py](/Examples/Module-1/m1-script2.py)
    
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
    
    [Example Script 3: m1-script3.py](/Examples/Module-1/m1-script3.py)
 
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
    [Example Script 4: m1-script4.py](/Examples/Module-1/m1-script4.py)

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
    [Example Script 5: m1-script5.py](/Examples/Module-1/m1-script5.py)

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
        
    [Example Script 6: m1-script6.py](/Examples/Module-1/m1-script6.py)
 
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
    [Example Script 7: m1-script7.py](/Examples/Module-1/m1-script7.py)
    
    - Assignment operators
    
        | operator |    description	                                                                                           | syntax            |
        |----------|-----------------------------------------------------------------------------------------------------------|------------------ |
        | =	       | assign value of right side of expression to left side operand	                                           | x = y + z         |  
        | +=	   | add and: add right side operand with left side operand and then assign to left operand	                   | a+=b  a=a+b       |
        | -=	   | subtract and: subtract right operand from left operand and then assign to left operand	                   | a-=b  a=a-b       |
        | *=	   | multiply and: multiply right operand with left operand and then assign to left operand	                   | a*=b  a=a*b       |
        | /=	   | divide and: divide left operand with right operand and then assign to left operand	                       | a/=b  a=a/b       |
        | %=	   | modulus and: takes modulus using left and right operands and assign result to left operand	               | a%=b  a=a%b       |
        | //=	   | divide(floor) and: divide left operand with right operand and then assign the value(floor) to left operand| a//=b a=a//b      |
        | **=	   | exponent and: calculate exponent(raise power) value using operands and assign value to left operand	   | a**=b a=a**b      |
        | &=	   | performs bitwise and on operands and assign value to left operand	                                       | a&=b  a=a&b       |
        | |=	   | performs bitwise or on operands and assign value to left operand	                                       | a|=b  a=a|b       |
        | ^=	   | performs bitwise xor on operands and assign value to left operand	                                       | a^=b  a=a^b       |
        | >>=	   | performs bitwise right shift on operands and assign value to left operand	                               | a>>=b a=a>>b      |
        | <<=	   | performs bitwise left shift on operands and assign value to left operand	                               | a <<= b a= a << b |

    [Example Script 8: m1-script8.py](/Examples/Module-1/m1-script8.py)

    - Special operators
    
        - Identity operators
            - **is** and **is not** are the identity operators both are used to check if two values are located on 
            the same part of the memory.
            
            ```html
              is          True if the operands are identical 
              is not      True if the operands are not identical 
            ```
            
            ```python

                # Examples of Identity operators 
                num_1 = 3
                num_2 = 3
                str_1 = 'PythonBasic'
                str_2 = 'PythonBasic'
                list_1 = [1,2,3] 
                list_2 = [1,2,3] 
                
                print(num_1 is not num_2)
                
                print(str_1 is str_2) 
                
                # Output is False, since lists are mutable. 
                print(list_1 is list_2) 

            ```
        [Example Script 9: m1-script9.py](/Examples/Module-1/m1-script9.py)
        
        - Membership operators
            - **in** and **not in** are the membership operators; used to test whether a value or variable is in a sequence. 
            ```html
              in            True if value is found in the sequence
              not in        True if value is not found in the sequence
            ```
            ```python

                # Examples of Membership operator 
                str_1 = 'Python Basic Training'
                dict_1 = {3:'a',4:'b'} 
                
                print('B' in str_1) 
                
                print('python' not in str_1) 
                
                print('Training' not in str_1) 
                
                print(3 in dict_1) 
                
                print('b' in dict_1) 
            
            ```
        [Example Script 10: m1-script10.py](/Examples/Module-1/m1-script10.py)

#
[Main...](https://github.com/ptoraskar/Python-Learning/blob/master/README.md) | [Back...](/Module-1/4_setup_python_environment.md) | [Next...](/Module-1/6_loops_and_conditions.md)


