#!/usr/bin/env python.


from test_class_1 import Parent

class Child(Parent):
    def __init__(self):
        print("Calling child constructor")

    def parent_method(self):
        print('Calling parent method in Child class')

    def child_method(self):
        print('Calling child method')
