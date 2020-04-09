
![](https://www.python.org/static/img/python-logo.png)
 
## Variables
### [Global Variables, Variable Scope and Returning Values]

- Declare and use a Variable
  ```python
    a=100
    print(a)
  ```

- Object References

    ```python
    n=300
    print(type(n))
    ```
    ![](/img/download.png)

- Object Identity

    ```python
    n=300
    print(id(n))    
    ```

- Delete a variable
  ```python
    a=100
    print(a)
    del a
  ```

- Deep Dive: Caching Small Integer Values

    ```python
      a = 300
      b = 300
    ```
    - With the statement a = 300, Python creates an integer object with the value 300 and sets m as a reference to it. 
    - b is then similarly assigned to an integer object with value 300 — but not the same object. 
    - Thus, they have different identities, which you can verify from the values returned by id().

    ```python
    print(id(a))
    print(id(b))
    ```
    
    ```python
      x = 50
      y = 50
    ```
    - Here, x and y are separately assigned to integer objects having value 50. 
    - But in this case, id(x) and id(x) are identical!
    - For purposes of optimization, the interpreter creates objects for the integers in the range [-5, 256] at startup, 
    and then reuses them during program execution.
    ```python
    print(id(x))
    print(id(y))
    ```
    
- Scope of Variables
    - Global variables
    - Local variables

    - Global vs. Local variables
        - Variables that are defined inside a function body have a local scope
        - Those defined outside have a global scope 

    ```python
    # This is global variable.
    total = 0
  
    # Function definition is here
    def get_sum( arg_1, arg_2 ):
       # Add both the parameters and return them."
       # Here total is local variable.
       sum_up = arg_1 + arg_2 
       print("Inside the function local sum : ", sum_up)
       return sum_up
    
    # Now you can call sum function
    get_sum( 10, 20 )
    print("Outside the function global total : ", total)     
    ```

    - A great of Example global variable
    ```python
        g_v = 1
        
        # Uses global because there is no local 'g_v' 
        def f_1(): 
            print('Inside f_1() : ', g_v) 
        
        # Variable 'G_V' is redefined as a local 
        def f_2(): 
            g_v = 2
            print('Inside f_2() : ', g_v) 
        
        # Uses global keyword to modify global 'g_v' 
        def f_3():	 
            global g_v
            g_v = 3
            print('Inside h() : ', g_v) 
        
        # Global scope 
        print('global variable: ',g_v)
        f_1() 
        print('global variable : ',g_v)
        f_2() 
        print('global variable : ',g_v)
        f_3()
        print('global variable : ',g_v)
    ```
    [Example Script 26 - m3-script26.py](/Examples/Module-3/m3-script26.py)
#
[Main...](https://github.com/ptoraskar/Python-Learning/blob/master/README.md) | [Next...](/Module-1/2_overview_to_python.md)
