  
![](https://www.python.org/static/img/python-logo.png)
 
## Python - Exceptions Handling
####*Types of Issues(Errors), Remediation, Exception Handling, Handling Multiple Exceptions*

 - Errors and Exceptions
    - Syntax Errors
    - Exceptions
    
    ```python
       while True print('Hello world')
        
       print(10 * (1/0))
       print(4 + spam*3)
       print('2' + 2)
     ```
    
 - Handling Exceptions
    - Python provides two very important features to handle any unexpected error in your Python programs and 
      to add debugging capabilities in them
        - Exception Handling 
        - Assertions
 
    ```python

       while True:
           try:
               x = int(input("Please enter a number: "))
               break
           except ValueError:
               print("Oops!  That was no valid number.  Try again...")
    ```
 - List of Standard Exceptions
 
     |Sr.No. | Exception | Description | 
     |---------|---------|---------|
     |1|Exception|Base class for all exceptions|
     |2|StopIteration|Raised when the next() method of an iterator does not point to any object.|
     |3|SystemExit|Raised by the sys.exit() function.|
     |4|StandardError|Base class for all built-in exceptions except StopIteration and SystemExit.|
     |5|ArithmeticError|Base class for all errors that occur for numeric calculation.|
     |6|OverflowError|Raised when a calculation exceeds maximum limit for a numeric type.|
     |7|FloatingPointError|Raised when a floating point calculation fails.|
     |8|ZeroDivisionError|Raised when division or modulo by zero takes place for all numeric types.|
     |9|AssertionError|Raised in case of failure of the Assert statement|
     |10|AttributeError|Raised in case of failure of attribute reference or assignment.|
     |11|EOFError|Raised when there is no input from either the raw_input() or input() function and the end of file is reached.|
     |12|ImportError|Raised when an import statement fails.|
     |13|KeyboardInterrupt|Raised when the user interrupts program execution, usually by pressing Ctrl+c.|
     |14|LookupError|Base class for all lookup errors.|
     |15|IndexError|Raised when an index is not found in a sequence.|
     |16|KeyError|Raised when the specified key is not found in the dictionary.|
     |17|NameError|Raised when an identifier is not found in the local or global namespace.|
     |18|UnboundLocalError|Raised when trying to access a local variable in a function or method but no value has been assigned to it.|
     |19|EnvironmentError|Base class for all exceptions that occur outside the Python environment.|
     |20|IOError|Raised when an input/ output operation fails, such as the print statement or the open() function when trying to open a file that does not exist.|
     |21|IOError|Raised for operating system-related errors.|
     |22|SyntaxError|Raised when there is an error in Python syntax.|
     |23|IndentationError|Raised when indentation is not specified properly.|
     |24|SystemError|Raised when the interpreter finds an internal problem, but when this error is encountered the Python interpreter does not exit.|
     |25|SystemExit|Raised when Python interpreter is quit by using the sys.exit() function. If not handled in the code, causes the interpreter to exit.
     |26|TypeError|Raised when an operation or function is attempted that is invalid for the specified data type.|
     |27|ValueError|Raised when the built-in function for a data type has the valid type of arguments, but the arguments have invalid values specified.|
     |28|RuntimeError|Raised when a generated error does not fall into any category.|
     |29|NotImplementedError|Raised when an abstract method that needs to be implemented in an inherited class is not actually implemented.|
     
 - A **try** statement may have more than one except clause, to specify handlers for different exceptions. 
    
    ```python
       try:
           pass
       except (RuntimeError, TypeError, NameError):
           pass
    ```
 - The **try … except** statement has an optional else clause, which, when present, must follow all except clauses    

    ```python
        import sys
     
        for arg in sys.argv[1:]:
            try:
                f = open(arg, 'r')
            except OSError:
                print('cannot open', arg)
            else:
                print(arg, 'has', len(f.readlines()), 'lines')
                f.close()       
    ```   
 - Raising Exceptions
    - The raise statement allows to force a specified exception to occur.
    ```python
        raise NameError('HiThere')

        try:
            raise NameError('HiThere')
        except NameError:
            print('An exception flew by!')
            raise
    ``` 

 - User-defined Exceptions

    ```python

        class Error(Exception):
            """Base class for exceptions in this module."""
            pass
        
        class InputError(Error):
            """Exception raised for errors in the input.
        
            Attributes:
                expression -- input expression in which the error occurred
                message -- explanation of the error
            """
        
            def __init__(self, expression, message):
                self.expression = expression
                self.message = message
        
        class TransitionError(Error):
            """Raised when an operation attempts a state transition that's not
            allowed.
        
            Attributes:
                previous -- state at beginning of transition
                next -- attempted new state
                message -- explanation of why the specific transition is not allowed
            """
        
            def __init__(self, previous, next, message):
                self.previous = previous
                self.next = next
                self.message = message
    ```

 - Clean-up Actions **finally()**

    - If a **finally** clause is present, the finally clause will execute as the last task before the try statement completes

    ```python

       def bool_return():
           try:
               return True
           finally:
               return False
       bool_return()
    ```
    
    [Example Script 28 - m3-script28.py](/Examples/Module-3/m3-script28.py)    
 
#
[Main...](https://github.com/ptoraskar/Python-Learning/blob/master/README.md) | [Next...](/Module-3/2_functions.md)