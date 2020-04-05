
![](https://www.python.org/static/img/python-logo.png)

## Command Line Arguments
- The arguments that are given after the name of the program in the command line shell of the operating system are 
  known as Command Line Arguments. 
  Most common way of dealing is using **sys.argv**
   
  [Example Script 16 m1-script16.py](/Examples/Module-1/m1-script16.py)

## Writing to the screen
- What is Console in Python? 
  - Console (also called Shell) is basically a command line interpreter that takes input from the user 
    - i.e one command at a time and interprets it. 
  - If it is error free then it runs the command and gives required output otherwise shows the error message. 
  - A Python Console looks like this.
  
  - Accepting Input from Console
  
  ```python

    # input 
    input1 = input() 

    # output 
    print(input1) 
    ```

  - Typecasting the input
    - Integer:
        ```python
          input1 = int(input())
        ````
    - Float
        ```python
          input1 = float(input())
        ````
    - String
        ```python
          input1 = str(input())
        ````

## Write your First Python Program

- Assignment 1: 
  Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.

- Assignment 2: 
  Write a Python program to calculate number of days between two dates..

- Assignment 3: 
  Write a Python program to print all even numbers from a given numbers list in the same order and stop the printing if any numbers that come after 237 in the sequence.
  ```python

    numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]
  ```

#
[Main...](https://github.com/ptoraskar/Python-Learning/blob/master/README.md) | [Back...](/Module-1/6_loops_and_conditions.md)


