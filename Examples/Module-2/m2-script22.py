
# Define Tuple
# ----------------
tup_1 = ('Berlin', 'London', 2019, 2020)
tup_2 = (1, 2, 3, 4, 5)
tup_3 = "a", "b", "c", "d"


# Accessing Values
# ----------------
print("tup1[0]: ", tup_1[0])
print("tup2[1:5]: ", tup_2[1:5])


# Updating Tuple
# ----------------
tup_1 = (12, 34.56)
tup_2 = ('abc', 'xyz')

# Following operation is invalid for tuples
# tup_1[0] = 100

# So let's create a new tuple as follows
tup_3 = tup_1 + tup_2
print(tup_3)


# Delete
# ----------------
tup_obj = ('Berlin', 'London', 2019, 2020)
print(tup_obj)
del tup_obj


# Length
# ----------------
print(len((1, 2, 3)))

# Concatenation
# ----------------
print((1, 2, 3) + (4, 5, 6))

# Repetition
# ----------------
print(('Hi!') * 4)

# Membership
# ----------------
print(3 in (1, 2, 3))

# Iteration
# ----------------
for x in (1, 2, 3): print(x)


# Indexing, Slicing, Matrixes
list_1 = ('Berlin', 'London', 2019, 2020)

print(list_1[2])
print(list_1[-2])
print(list_1[1:])