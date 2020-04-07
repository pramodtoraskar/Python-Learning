""" This is python script: Explain decision making or Loop Statement!"""

# Python program to illustrate Iterating over a list
print("List Iteration")

list_1 = ["geeks", "for", "geeks"]

for list_ele in list_1:
    print(list_ele)

# Iterating over a String
print("\nString Iteration")
str_1 = "Geeks"
for str_ele in str_1:
    print(str_ele)

print("\nFor-else loop")
for str_ele in str_1:
    print(str_ele)
else:  # Executed because no break in for
    print("No Break\n")

for str_ele in str_1:
    print(str_ele)
    break
else:  # Not executed as there is a break
    print("No Break")
