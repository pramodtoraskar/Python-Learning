
class Parent():
    parent_attr = 100

    def __init__(self):
        self.__test_var = 2020
        print("Calling parent constructor")

    def __parent_method(self):
        print(self.test_var)
        print('Calling parent method')

    def set_attr(self, attr):
        Parent.parent_attr = attr
        self.__test_var = 2030

    def get_attr(self):
        print("Parent attribute :", Parent.parent_attr)
        print("Test Var: ", self.__test_var)
