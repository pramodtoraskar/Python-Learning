
![](https://www.python.org/static/img/python-logo.png)

## Python - Object Oriented

 - Python has been an object-oriented language since it existed
 - OOP Terminology
    - Class 
    - Class Variable
        - A variable that is shared by all instances of a class. 
        - Class variables are defined within a class but outside any of the class's methods.
    - Data member 
        - A class variable or instance variable that holds data associated with a class and its objects.
    - Function overloading 
        - The assignment of more than one behavior to a particular function. 
        - The operation performed varies by the types of objects or arguments involved.
    - Instance variable 
        - A variable that is defined inside a method and belongs only to the current instance of a class.
    - Inheritance 
        - The transfer of the characteristics of a class to other classes that are derived from it.
    - Instance 
        - An individual **object** of a certain class. 
    - Instantiation 
        - The creation of an instance of a class.
    - Method 
        - A special kind of function that is defined in a class definition.
    - Object 
        - A unique instance of a data structure that's defined by its class. 
        - An object comprises both data members (class variables and instance variables) and methods.
    - Operator overloading
        - The assignment of more than one function to a particular operator.

    ```python

    class MyTestClass:
        """A simple example class"""
        i = 12345
    
        def test_func(self):
            return 'hello world'      
    
    x = MyTestClass()
    ```
    - The instantiation operation (“calling” a class object) creates an empty object.
    - When a class defines an __init__() method, 
    - **class** instantiation automatically invokes __init__() for the newly-created class instance.
    
    ```python
    def __init__(self):
        pass
    ``` 

 -  Instantiation and Accessing Attributes
     
    ```python

    class Employee():
       """Common base class for all employees"""
       emp_count = 0
    
       def __init__(self, name, salary):
          self.name = name
          self.salary = salary
          Employee.emp_count += 1
       
       def display_count(self):
         print("Total Employee %d" % Employee.emp_count)
    
       def display_employee(self):
          print("Name : ", self.name,  ", Salary: ", self.salary)
    
    # "This would create first object of Employee class"
    emp1 = Employee("Pramod", 1545)
    # "This would create second object of Employee class"
    emp2 = Employee("Mahesh", 5000)
 
    emp1.display_employee()
    emp2.display_employee()
 
    print("Total Employee %d" % Employee.emp_count)
    ```

 - Built-In Class Attributes
    - __dict__ 
        - Dictionary containing the class's namespace
    - __doc__ 
        - Class documentation string or none, if undefined
    - __name__ 
        - Class name
    - __module__ 
        - Module name in which the class is defined. 
        - This attribute is "__main__" in interactive mode.
    - __bases__ 
        - A possibly empty tuple containing the base classes, in the order of their occurrence in the base class list.
        
    ```python

        print("Employee.__doc__:", Employee.__doc__)
        print("Employee.__name__:", Employee.__name__)
        print("Employee.__module__:", Employee.__module__)
        print("Employee.__bases__:", Employee.__bases__)
        print("Employee.__dict__:", Employee.__dict__)
    ```

 - Class Inheritance
    - Instead of starting from scratch, you can create a class by deriving it from a preexisting class
    ```python
        # Define parent class
        class Parent():        
           parent_attr = 100
           def __init__(self):
              print("Calling parent constructor")
        
           def parent_method(self):
              print('Calling parent method')
        
           def set_attr(self, attr):
              Parent.parentAttr = attr
        
           def get_attr(self):
              print("Parent attribute :", Parent.parent_attr)
        
        # Define child class
        class Child(Parent): 
           def __init__(self):
              print("Calling child constructor")
        
           def child_method(self):
              print('Calling child method')
        
        # Instance of child
        c = Child()        
     
        # Child calls its method
        c.child_method()
           
        # Calls parent's method
        c.parent_method()
          
        # Again call parent's method
        c.set_attr(200)       
     
        # Again call parent's method        
        c.get_attr()          
    ```

 - Overriding Methods
    - You can always override your parent class methods.
    - You achieve special or different functionality in your subclass.
    ```python
        # Define parent class
        class Parent():        
           def my_method(self):
              print('Calling parent method')

        # Define child class
        class Child(Parent):
           def my_method(self):
              print('Calling child method')
        
        # Instance of child
        c = Child()
             
        # Child calls overridden method
        c.my_method()             
    ```
  
 - Overloading Operators
 
     ```python
        # Function to take multiple arguments 
        def add(data_type, *args): 
        
            # if data_type is int initialize answer as 0 
            if data_type =='int': 
                answer = 0
                
            # if data_type is str initialize answer as '' 
            if data_type =='str': 
                answer ='' 
        
            # Traverse through the arguments 
            for x in args:         
                # This will do addition if the arguments are int. Or concatenation if the arguments are str 
                answer = answer + x 
        
            print(answer) 
        
        # Integer 
        add('int', 5, 6) 
        
        # String 
        add('str', 'Hi ', 'Pythonista')
    ```
    
 - Data Hiding
    - An object's attributes may or may not be visible outside the class definition
    ```python
        class JustCounter():
           __secret_count = 0
          
           def count(self):
              self.__secret_count += 1
              print(self.__secret_count)
        
        counter = JustCounter()
        counter.count()
        counter.count()
        print(counter.__secret_count)
    ```
    
  [Example Script 29 - m3-script29.py](/Examples/Module-3/m3-script29.py)
 #
[Main...](https://github.com/ptoraskar/Python-Learning/blob/master/README.md) | [Next...](/Module-3/2_functions.md)