
# Functions

Functions are a convenient way to divide your code into useful blocks, allowing us to order our code, make it more readable, reuse it and save some time. 
Also functions are a key way to define interfaces so programmers can share their code.

Python gives you many built-in functions like print()

**How do you write functions in Python?**

```Syntax
block_head: 
    1st block line 
    2nd block line 
```

Functions in python are defined using the block keyword "def", followed with the function's name as the block's name. For example:
The first statement of a function can be an optional statement - the documentation string of the function or docstring.
The code block within every function starts with a colon (:) and is indented.
The statement return [expression] exits a function, optionally passing back an expression to the caller. 

Note: A return statement with no arguments is the same as return None.

```python
def printme( str ):
   "This prints a passed string into this function"
   print str
   return
```

**How do you call functions in Python?**

Once the basic structure of a function is finalized, Simply write the function's name followed by (), placing any required arguments within the brackets. 

Following is the example to call printme() function −
```python
#!/usr/bin/python

# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print str
   return;

# Now you can call printme function
printme("I'm first call to user defined function!")
printme("Again second call to the same function")


When the above code is executed, it produces the following result −

I'm first call to user defined function!
Again second call to the same function
```


#### Pass by reference vs value
All parameters (arguments) in the Python language are passed by reference.
It means if you change what a parameter refers to within a function, the change also reflects back in the calling function.

For example −
```python
#!/usr/bin/python

# Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist.append([10,25,39,40]);
   print "Values inside the function: ", mylist
   return

# Now you can call changeme function
mylist = [1,2,3];
changeme( mylist );
print "Values outside the function: ", mylist
```

#### Function Arguments
You can call a function by using the following types of formal arguments:

1. Required arguments
2. Keyword arguments
3. Default arguments
5. Variable-length arguments

#### The Anonymous Functions

These functions are called anonymous because they are not declared in the standard manner by using the def keyword. You can use the lambda keyword to create small anonymous functions.

Syntax
```
lambda [arg1 [,arg2,.....argn]]:expression
```
For example
```python
#!/usr/bin/python

# Function definition is here
sum = lambda arg1, arg2: arg1 + arg2;

 

# Now you can call sum as a function
print "Value of total : ", sum( 100, 200 )
print "Value of total : ", sum( 200, 200 )
```
When the above code is executed, it produces the following result −
```
Value of total :  300
Value of total :  400
```
