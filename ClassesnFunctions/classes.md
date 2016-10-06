# Class / Object Oriented

You can think about a module as a specialized dictionary that can store Python code so you can access it with the . operator. 
Python also has another construct that serves a similar purpose called a class. A class is a way to take a grouping of functions and data and place them inside a container so you can access them with the . (dot) operator.

If I were to create a class just like the mystuff module, I'd do something like this:

```python

class MyStuff(object):

    variable = "blah"
    
    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print "I AM CLASSY APPLES!"

```

**Defination**:

Objects are an encapsulation of variables and functions into a single entity. Objects get their variables and functions from classes. Classes are essentially a template to create your objects.

To assign the above class(template) to an object you would do the following:
```python
myobjectx = MyStuff()
```
**Accessing Object Variables**

To access the variable inside of the newly created object "myobjectx" you would do the following:

```python
myobjectx.variable
```

You can create multiple different objects that are of the same class(have the same variables and functions defined). 
However, each object contains independent copies of the variables defined in the class. 

For instance, if we were to define another object with the "MyStuff" class and then change the string in the variable above:
```python
myobjecty = MyStuff()
myobjecty.variable = "yackity"
```

Then print out both values:
```python
print myobjectx.variable   # This would print "blah".
print myobjecty.variable   # This would print "yackity".
```

To access a function inside of an object you use notation similar to accessing a variable:
```python
myobjectx.function()
```

**Built-In Class Attributes**

Every Python class keeps following built-in attributes and they can be accessed using dot operator like any other attribute −

__dict__: Dictionary containing the class's namespace.
__doc__: Class documentation string or none, if undefined.
__name__: Class name.
__module__: Module name in which the class is defined. This attribute is "__main__" in interactive mode.
__bases__: A possibly empty tuple containing the base classes, in the order of their occurrence in the base class list.



**Destroying Objects (Garbage Collection)**

Python deletes unneeded objects (built-in types or class instances) automatically to free the memory space. The process by which Python periodically reclaims blocks of memory that no longer are in use is termed Garbage Collection.

Python's garbage collector runs during program execution and is triggered when an object's reference count reaches zero. An object's reference count changes as the number of aliases that point to it changes.

An object's reference count increases when it is assigned a new name or placed in a container (list, tuple, or dictionary). The object's reference count decreases when it's deleted with del, its reference is reassigned, or its reference goes out of scope. When an object's reference count reaches zero, Python collects it automatically.
```
a = 40      # Create object <40>
b = a       # Increase ref. count  of <40> 
c = [b]     # Increase ref. count  of <40> 

del a       # Decrease ref. count  of <40>
b = 100     # Decrease ref. count  of <40> 
c[0] = -1   # Decrease ref. count  of <40>
 ```
You normally will not notice when the garbage collector destroys an orphaned instance and reclaims its space. But a class can implement the special method __del__(), called a destructor, that is invoked when the instance is about to be destroyed. This method might be used to clean up any non memory resources used by an instance.

Example
This __del__() destructor prints the class name of an instance that is about to be destroyed −
```python
#!/usr/bin/python

class Point:
   def __init( self, x=0, y=0):
      self.x = x
      self.y = y
   def __del__(self):
      class_name = self.__class__.__name__
      print class_name, "destroyed"

pt1 = Point()
pt2 = pt1
pt3 = pt1
print id(pt1), id(pt2), id(pt3) # prints the ids of the obejcts
del pt1
del pt2
del pt3
```
When the above code is executed, it produces following result −
```
3083401324 3083401324 3083401324
```
Point destroyed
Note: Ideally, you should define your classes in separate file, then you should import them in your main program file using import statement.