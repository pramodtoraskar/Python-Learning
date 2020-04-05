
![](https://www.python.org/static/img/python-logo.png)

## Conditional Statements / Decision Making
 - In programming is similar to decision making in real life. 
 - A programming language uses control statements to control the flow of execution of the program based on certain conditions. 
 - These are used to cause the flow of execution to advance and branch based on changes to the state of a program.

    ```html
    if statement
    if..else statements
    nested if statements
    if-elif ladder
    ```
    
    ```python
        # Python program to demonstrate decision making
        
        num_1 = 10
        num_2 = 15
        
        # if to check even number 
        if num_1 % 2 == 0: 
            print("Even Number") 
            
        # if-else to check even or odd 
        if num_2 % 2 == 0: 
            print("Even Number") 
        else: 
            print("Odd Number")

    ```
    [Example Script 11: m1-script11.py](/Examples/Module-1/m1-script11.py)

    **nested-if and if-elif**
       
    ```python
        # Python program to demonstrate decision makings 

        num_1 = 10
        
        # Nested if to check whether num_1 number is divisible by both 2 and 5 
        if num_1 % 2 == 0: 
            if num_1 % 5 == 0: 
                print("Number is divisible by both 2 and 5") 
        
        # is-elif 
        if num_1 == 11: 
            print ("num_1 is 11") 
        elif num_1 == 10: 
            print ("num_1 is 10") 
        else: 
            print ("num_1 is not present")
    ```
    
    [Example Script 12: m1-script12.py](/Examples/Module-1/m1-script12.py)
    
 - Single Statement Suites
    - If the suite of an if clause consists only of a single line, it may go on the same line as the header statement.
    
    ```python
       num_var = 100
       if num_var == 100: print("Value of expression is 100")
       print("Good bye!")
    ```
    
## Loops

 - Loops in programming come into use when we need to repeatedly execute a block of statements. 
 - For example: Suppose we want to print “Hello World” 10 times. 
 - This can be done with the help of loops. The loops in Python are:
    -  While and while-else loop

        ```python
            # Python program to illustrate while and while-else loop 
            num_1 = 0
            while num_1 < 3:	 
                num_1 = num_1 + 1
                print("Hello Geek") 
                
            # checks if list still contains any element 
            list_1 = [1, 2, 3, 4] 
            while list_1: 
                print(list_1.pop()) 
                
            num_1 = 10
            while num_1 < 12: 
                num_1 += 1
                print(num_1) 
                break
            else: # Not executed as there is a break 
                print("No Break") 
     
        ```
        [Example Script 12: m1-script12.py](/Examples/Module-1/m1-script12.py)
 
    - For and for-else loop
        ```python
            # Python program to illustrate Iterating over a list 
            print("List Iteration") 
            list_1 = ["geeks", "for", "geeks"] 
            for list_ele in list_1: 
                print(list_ele) 
                
            # Iterating over a String 
            print("\nString Iteration")	 
            str_1 = "Geeks"
            for str_ele in str_1: 
                print(str_ele) 
                
            print("\nFor-else loop") 
            for str_ele in str_1: 
                print(str_ele) 
            else: # Executed because no break in for 
                print("No Break\n") 
                
            for str_ele in str_1: 
                print(str_ele) 
                break
            else: # Not executed as there is a break 
                print("No Break")
        ```
        [Example Script 13: m1-script13.py](/Examples/Module-1/m1-script13.py)

- `range()` function
    - Allows user to generate a series of numbers within a given range.
        -   This function takes three arguments.
            -   start: integer starting from which the sequence of integers is to be returned
            -   stop: integer before which the sequence of integers is to be returned.
            -   step: integer value which determines the increment between each integer in the sequence filter_none 

        ```python
            # Python program to demonstrate range() function
            
            for ele in range(5): 
                print(ele, end =" ") 
            print() 
            
            for ele in range(2, 9): 
                print(ele, end =" ") 
            print() 
            
            # incremented by 3 
            for ele in range(15, 25, 3): 
                print(ele, end =" ") 
        ```
        [Example Script 14 m1-script14.py](/Examples/Module-1/m1-script14.py)        

- Loop control statements
    - Loop control statements change execution from its normal sequence
        - Break: Break statement in Python is used to bring the control out of the loop when some external condition is triggered.
        - Continue: Continue statement is opposite to that of break statement, instead of terminating the loop, it forces to execute the next iteration of the loop.
        - Pass: Pass statement is used to write empty loops. Pass is also used for empty control statement, function and classes.
        
       ```python
            # Python program to demonstrate break, continue and pass 
            str_1 = 'pythonbasictraning'
            
            for letter in str_1: 
                if letter == 'n' or letter == 'r': 
                    break
                print(letter, end = " ") 
            print() 
            
            for letter in str_1: 
                if letter == 'c' or letter == 'g': 
                    continue
                print(letter, end = " ") 
            print()	 
            
            for letter in str_1: 
                if letter == 'i' or letter == 'ni': 
                    pass
                print(letter, end = " ") 
        
        ```
       [Example Script 15 m1-script15.py](/Examples/Module-1/m1-script15.py)

#
[Main...](https://github.com/ptoraskar/Python-Learning/blob/master/README.md) | [Back...](/Module-1/5_variables_to_expressions.md) | [Next...](/Module-1/7_command_line_and_python_program.md)


