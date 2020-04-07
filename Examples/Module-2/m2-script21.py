
# Define List
# ----------------
list_1 = ['Berlin', 'London', 2019, 2020]
list_2 = [1, 2, 3, 4, 5];
list_3 = ["a", "b", "c", "d"]

# Accessing values in string
# ----------------
print("list1[0]: ", list_1[0])
print("list2[1:5]: ", list_2[1:5])


# Updating List
# ----------------
list_obj = ['Berlin', 'London', 2019, 2020]

print("Value available at index 2 : ")

print(list_obj[2])
list_obj[2] = 2021;

print("New value available at index 2 : ")
print(list_obj[2])

# Length
# ----------------
print(len([1, 2, 3]))

# Concatenation
# ----------------
print([1, 2, 3] + [4, 5, 6])

# Repetition
# ----------------
print(['Hi!'] * 4)

# Membership
# ----------------
print(3 in [1, 2, 3])

# Iteration
# ----------------
for x in [1, 2, 3]: print(x)


# Indexing, Slicing, Matrixes
list_1 = ['Berlin', 'London', 2019, 2020]

print(list_1[2])
print(list_1[-2])
print(list_1[1:])