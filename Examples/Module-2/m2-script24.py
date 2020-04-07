
# Define Tuple
# ----------------
set_obj = {'E1', 'E2', 'E3'}

# Program to demonstrate adding elements in a set

# Creating a Set
attendees = {"Amit", "Nikita", "Sanjeevani", "Vikram"}
print("Attendees:", end=" ")
print(attendees)

# This will add Daxit in the set
attendees.add("Sagar")

# Adding elements to the set using iterator
for i in range(1, 6):
    attendees.add(i)

print("\nSet after adding element:", end=" ")
print(attendees)

# Union
# Program to demonstrate union of two sets
# ----------------
attendees = {"Amit", "Nikita", "Sanjeevani", "Vikram"}
assignment_complete = {"Dushyen", "Reetika"}
assignment_not_complete = {"Pramod", "Mahesh"}

# Union using union() function
attendees_assignment = attendees.union(assignment_complete)

print("Union using union() function")
print(attendees_assignment)

# Union using "|" operator
participants = assignment_complete|assignment_not_complete

print("\nUnion using '|' operator")
print(participants)

# Intersection
# Program to demonstrate intersection of two sets
# ----------------
attendees = {"Amit", "Nikita", "Sanjeevani", "Vikram"}
assignment_complete = {"Dushyen", "Nikita"}
assignment_not_complete = {"Pramod", "Amit"}

# Intersection using intersection() function
attendees_inter = attendees.intersection(assignment_complete)

print("Intersection using intersection() function")
print(attendees_inter)

# Intersection using "&" operator
attendees_inter = attendees & assignment_not_complete

print("\nIntersection using '&' operator")
print(attendees_inter)

# Difference
# Program demonstrate difference of two sets
# ----------------
attendees = {"Amit", "Nikita", "Sanjeevani", "Vikram"}
assignment_complete = {"Dushyen", "Nikita"}
assignment_not_complete = {"Pramod", "Amit"}

# Difference of two sets using difference() function
attendees_diff = attendees.difference(assignment_complete)

print(" Difference of two sets using difference() function")
print(attendees_diff)

# Difference of two sets
# using '-' operator
attendees_diff = attendees - assignment_complete

print("\nDifference of two sets using '-' operator")
print(attendees_diff)


# Python program to demonstrate working# of Set in Python

# Creating two sets
set_1 = set()
set_2 = set()

# Adding elements to set_1
for i in range(1, 6):
    set_1.add(i)

# Adding elements to set_2
for i in range(3, 8):
    set_2.add(i)

print("set_1 = ", set_1)
print("set_2 = ", set_2)
print("\n")

# Union of set_1 and set_2
# set_1.union(set_2)
set_3 = set_1 | set_2 
print("Union of set_1 & set_2: set_3 = ", set_3)

# Intersection of set_1 and set_2
# set_1.intersection(set_2)
set_4 = set_1 & set_2
print("Intersection of set_1 & set_2: set_4 = ", set_4)
print("\n")

# Checking relation between set3 and set_4

# set_3.issuperset(set_4)
if set_3 > set_4:
    print("set_3 is superset of set_4")
# set_3.issubset(set_4)
elif set_3 < set_4:
    print("set_3 is subset of set_4")
# set_3 == set_4
else:
    print("set_3 is same as set_4")

# displaying relation between set_4 and set_3
# set_4.issubset(set_3)
if set_4 < set_3:
    print("set_4 is subset of set_3")
    print("\n")

# difference between set_3 and set_4
set_5 = set_3 - set_4
print("Elements in set_3 and not in set_4: set_5 = ", set_5)
print("\n")

# check if set_4 and set_5 are disjoint sets
if set_4.isdisjoint(set_5):
    print("set_4 and set_5 have nothing in common\n")

# Removing all the values of set_5
set_5.clear()

print("After applying clear on sets set_5: ")
print("set_5 = ", set_5)
