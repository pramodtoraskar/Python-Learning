# Classes and Class Creation

#### New-style vs. old-style Classes

"New-style classes were introduced in Python 2.2 to unify classes and types. A new-style class neither more nor less than a user-defined type. If x is an instance of a new-style class, then type(x) is the same as x.class."

The next paragraph informs us about the motivation for introducing new-style classes. They are needed "to provide a unified object model with a full meta-model". They mention as other "immediate benefits" the "ability to subclass most built-in types, or the introduction of 'descriptors', which enable computed properties."

We don't want to dive into all the subtleties of old-style classes. Don't think about it as an option to choose from: There should be only one style for you to use: the new-style class!

There is only a minor syntactic difference, which can easily be overlooked: A class can only be a new-style class, if it inherits from object or from another new-style class. Python 3 only has new-style classes.

```python
# old-style class
class A:
    pass
class B(A):
    pass
a = A()
b = B()
print(type(A), type(B))
print(type(a), type(b))
```
After having executed the Python code above we received the following:
(<type 'classobj'>, <type 'classobj'>)
(<type 'instance'>, <type 'instance'>)

```python
# new-style class
class A(object):
    pass
class B(A):
    pass
a = A()
b = B()
print(type(A), type(B))
print(type(a), type(b))
```
The Python code above returned the following:
```python
(<type 'type'>, <type 'type'>)
(<class '__main__.A'>, <class '__main__.B'>)
```

The new method creates and returns the new class object, and after this the init method initializes the newly created object.
```python
class Robot(object):
    counter = 0
    def __init__(self, name):
        self.name = name
    def sayHello(self):
        return "Hi, I am " + self.name
def Rob_init(self, name):
    self.name = name
Robot2 = type("Robot2", 
              (), 
              {"counter":0, 
               "__init__": Rob_init,
               "sayHello": lambda self: "Hi, I am " + self.name})
x = Robot2("Marvin")
print(x.name)
print(x.sayHello())
y = Robot("Marvin")
print(y.name)
print(y.sayHello())
print(x.__dict__)
print(y.__dict__)
```
We received the following output:
```
Marvin
Hi, I am Marvin
Marvin
Hi, I am Marvin
{'name': 'Marvin'}
{'name': 'Marvin'}
```

The class definitions for Robot and Robot2 are syntactically completely different, but they implement logically the same class.

What Python actually does in the first example, i.e. the "usual way" of defining classes, is the following: Python processes the complete class statement from class Robot to collect the methods and attributes of Robot to add them to the attributes_dict of the type call. So, Python will call type in a similar way than we did in Robot2.