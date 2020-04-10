

# Example of Class
# ------------------------------------------
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
        print("Name : ", self.name, ", Salary: ", self.salary)


# "This would create first object of Employee class"
emp1 = Employee("Pramod", 1545)
# "This would create second object of Employee class"
emp2 = Employee("Mahesh", 5000)

emp1.display_employee()
emp2.display_employee()

print("Total Employee %d" % Employee.emp_count)
print("Employee.__doc__:", Employee.__doc__)
print("Employee.__name__:", Employee.__name__)
print("Employee.__module__:", Employee.__module__)
print("Employee.__bases__:", Employee.__bases__)
print("Employee.__dict__:", Employee.__dict__)


# Example of Inheritance
# ------------------------------------------
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


# Example of Overriding Methods
# ------------------------------------------
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


# Example of Overloading Operators
# ------------------------------------------
def add(data_type, *args):
    # if data_type is int initialize answer as 0
    if data_type == 'int':
        answer = 0

    # if data_type is str initialize answer as ''
    if data_type == 'str':
        answer = ''

        # Traverse through the arguments
    for x in args:
        # This will do addition if the arguments are int. Or concatenation if the arguments are str
        answer = answer + x

    print(answer)


# Integer
add('int', 5, 6)

# String
add('str', 'Hi ', 'Pythonista')


# Example of Data Hiding
# ------------------------------------------
class JustCounter():
    __secret_count = 0

    def count(self):
        self.__secret_count += 1
        print(self.__secret_count)

counter = JustCounter()
counter.count()
counter.count()

# Un-comment for Demo
# print(counter.__secret_count)
