
 
 
![](https://www.python.org/static/img/python-logo.png)
 
## Lambda
###Features, Syntax, Options, Compared with the Functions

 - Anonymous function means that a function is without a name
 - **def**s keyword is used to define the normal functions
 - the **lambda** keyword is used to create anonymous functions

    > lambda arguments: expression

    ```python
        # Code to illustrate cube of a number showing difference between def() and lambda().
    
        def cube(y):
            return y*y*y 
        
        g = lambda x: x*x*x 
        
        print(g(7)) 
        print(cube(5)) 
    ```
    
 - **Without** using **Lambda**
    - Both of them returns the cube of a given number. 
    - But, while using **def**, we needed to define a function with a name cube and needed to pass a value to it. 
    - After execution, we also needed to return the result from where the function was called using the return keyword.
 - Using **Lambda**
    - Lambda definition does not include a “return” statement, it always contains an expression which is returned. 
    - We can also put a lambda definition anywhere a function is expected, and we don’t have to assign it to a variable at all. 
    - This is the simplicity of lambda functions.    

- Used along with built-in functions <br/>
    *filter(), map() and reduce()*
    
    - The filter() function in Python takes in a function and a list as arguments. 
    - This offers an elegant way to filter out all the elements of a sequence “sequence”, for which the function 
    returns True. 

    ```python
       # Code to illustrate filter() with lambda()
     
       list_1 = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
     
       final_list = list(filter(lambda x: (x % 2 != 0) , list_1))
     
       print(final_list)
    ```
    
    - The map() function in Python takes in a function and a list as argument. 
    - The function is called with a lambda function and a list and a new list is returned which contains all the lambda 
    modified items returned by that function for each item. 

    ```python
        
      # Code to illustrate map() with lambda() to get double of a list. 
      list_1 = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
     
      final_list = list(map(lambda x: x*2 , list_1))
     
      print(final_list)
    ```
    
    - The reduce() function in Python takes in a function and a list as argument. 
    - The function is called with a lambda function and a list and a new reduced result is returned. 
    - This performs a repetitive operation over the pairs of the list. This is a part of functools
    ```python

      # Code to illustrate reduce() with lambda() to get sum of a list
      
      from functools import reduce
    
      list_1 = [5, 8, 10, 20, 50, 100]
     
      sum_num = reduce((lambda x, y: x + y), list_1)
     
      print (sum_num) 
      
    ```

  [Example Script 27 - m3-script27.py](/Examples/Module-3/m3-script27.py)

`
#
[Main...](https://github.com/ptoraskar/Python-Learning/blob/master/README.md) | [Next...](/Module-3/5_Sorting.md)