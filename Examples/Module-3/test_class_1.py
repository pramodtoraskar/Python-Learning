
class Parent():
    parent_attr = 100

    def __init__(self):
        print("Calling parent constructor")

    def parent_method(self):
        print('Calling parent method')

    def set_attr(self, attr):
        Parent.parent_attr = attr

    def get_attr(self):
        print("Parent attribute :", Parent.parent_attr)
