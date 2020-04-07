""" This is python script: Explain decision making or Conditional Statement!"""

# Python program to demonstrate nested-if and if-elif

num_1 = 10

# Nested if to check whether num_1 number is divisible by both 2 and 5
if num_1 % 2 == 0:
    if num_1 % 5 == 0:
        print("Number is divisible by both 2 and 5")

    # is-elif
if num_1 == 11:
    print("num_1 is 11")
elif num_1 == 10:
    print("num_1 is 10")
else:
    print("num_1 is not present")
