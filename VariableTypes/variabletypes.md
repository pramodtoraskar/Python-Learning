
# Variable Types
 Reserved memory locations to store values are nothing but Variables. This means that when you create a variable you reserve some space in memory.
 Based on the data type of a variable, the python interpreter allocates memory and decides what can be stored in the reserved memory. 

## Assigning Values to Variables
 In python variables do not need explicit declaration to reserve memory space. 
 The declaration happens automatically when you assign a value to a variable. The equal sign (=) is used to assign values to variables.
 The operand to the left of the = operator is the name of the variable and the operand to the right of the = operator is the value stored in the variable. 

 For example −
```python
#!/usr/bin/python

counter = 50          # An integer assignment
miles   = 100.0       # A floating point
name    = "python"    # A string

print counter
print miles
print name
```

## Multiple Assignment
 Python allows programmer to assign a single value to several variable simultaneously.

 For example - 
```python
   a = b = c = 4
```

 All three variables are assigned to the same memory location.
 You can also assign multiple objects to multiple variables 
 
 For example -
```python
   a, b, c = 1, 2, 'python'
```

## Standard Data Types
 Python has five standard data types -
 ..* Numbers
 ..* String
 ..* List
 ..* Tuple
 ..* Dictinoary
 
## Numbers
 Number objects are created when you assign a value to them. Number data types store numeric values 
 For example -
 
```python
   num1 = 5
   num2 = 10
```

 There are four different numerical data types - 
 ..* int ( single integers )
 ..* long ( Long integers have unlimited precision )
 ..* float ( floating points real values )
 ..* complex ( complex number have a real and imaginary part )
 
## Strings
 A contiguous set of characters reprsented in the quotation marks.
 Python program allows for either pairs of single '' or double "" quotes.
 
 Slice Operation:
 
 The slice operator ([] and [:]) with indexes starting at 0 in then beginning of the string
 In string reverse start from -1 
  
 For example - 
```python

   str_obj = "Hellow python!"
   
   print str_obj             # Prints entier string
   print str_obj[0]          # Prints first character of the string
   print str_obj[2:5]        # Prints characters starting from 3rd to 5th
   print str[2:]             # Prints string starting from 3rd character
   print str * 2             # Prints string two times
   print str + "Demo"        # Prints concatenated string
```
 
## Lists

## Tuples

## Dictionary

## Data Type Conversion