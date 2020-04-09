

# Difference between def() and lambda().
# ---------------------------------------------------------------------
def cube(y):
    return y * y * y


g = lambda x: x * x * x

print(g(7))
print(cube(5))


#  filter() with lambda()
# ---------------------------------------------------------------------
# Code to illustrate filter() with lambda()

list_1 = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

final_list = list(filter(lambda x: (x % 2 != 0), list_1))

print(final_list)


# map() with lambda()
# ---------------------------------------------------------------------
# Code to illustrate map() with lambda() to get double of a list.
list_1 = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

final_list = list(map(lambda x: x * 2, list_1))

print(final_list)


# reduce() with lambda()
# ---------------------------------------------------------------------
# Code to illustrate reduce() with lambda() to get sum of a list
from functools import reduce

list_1 = [5, 8, 10, 20, 50, 100]

sum_num = reduce((lambda x, y: x + y), list_1)

print(sum_num)