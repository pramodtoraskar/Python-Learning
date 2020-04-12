from test_class_1 import Parent

class Child(Parent):
    def __init__(self):
        print("Calling child constructor")

    def child_method(self):
        print('Calling child method')
