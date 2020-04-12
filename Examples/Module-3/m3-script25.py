

# Python function
# ---------------------------------------------------------------------------
def even_odd_fun(x):
    if x % 2 == 0:
        print("even")
    else:
        print("odd")


# Call function
even_odd_fun(2)
even_odd_fun(3)


# Example of Default arguments
# ---------------------------------------------------------------------------
def test_fun(x, y=50):
    print("x: ", x)
    print("y: ", y)


# Call test_fun() with only argument
test_fun(10)


# Example of Keyword arguments
# ---------------------------------------------------------------------------
def student_info(first_name, last_name):
    print(first_name, last_name)


# Keyword arguments
student_info(first_name='Ankitkumar', last_name='Rajput')
student_info(last_name='Inder', first_name='Punj')


# Example of Variable length arguments
# ---------------------------------------------------------------------------
# Python program to illustrate *args for variable number of arguments
def test_args_list_fun(*argv):
    for arg in argv:
        print(arg)


test_args_list_fun('Hello', 'Welcome', 'to', 'RedHat!')


# Program to illustrate *kargs for variable number of keyword arguments
def test_args_dict_fun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


test_args_dict_fun(first='Pramod', mid='S', last='Toraskar')


# Example of Anonymous functions
# ---------------------------------------------------------------------------
# Code to illustrate cube of a number using labmda function
get_cube = lambda x: x * x * x
print(get_cube(7))


# Example of Pass by reference vs value
# ---------------------------------------------------------------------------
def change_param(list_obj):
    """This changes a passed list into this function"""
    list_obj.append([1, 2, 3, 4])
    print("Values inside the function: ", list_obj)
    return

# Call change_param function
list_obj = [10, 20, 30]
change_param(list_obj)
print("Values outside the function: ", list_obj)


def change_param(list_obj):
    """This changes a passed list into this function"""
    list_obj = [1, 2, 3, 4]
    print("Values inside the function: ", list_obj)
    return


# Call change_param function
list_obj = [10, 20, 30]
change_param(list_obj)
print("Values outside the function: ", list_obj)


# Example of Return Values
# ---------------------------------------------------------------------------
def get_num_sum(arg1, arg2):
    """Add both the parameters and return them."""
    num_total = arg1 + arg2
    print("Inside the function : ", num_total)
    return num_total


# Now you can call sum function
get_total = get_num_sum(10, 20)
print("Outside the function : ", get_total)
