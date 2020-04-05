""" This is python script: range() function!"""

# Python program to demonstrate break, continue and pass
str_1 = 'pythonbasictraning'

for letter in str_1:
    if letter == 'n' or letter == 'r':
        break
    print(letter, end=" ")
print()

for letter in str_1:
    if letter == 'c' or letter == 'g':
        continue
    print(letter, end=" ")
print()

for letter in str_1:
    if letter == 'i' or letter == 'ni':
        pass
    print(letter, end=" ")
