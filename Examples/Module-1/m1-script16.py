""" Python program to demonstrate command line arguments"""

import sys

"""
  It is a list of command line arguments.
  len(sys.argv) provides the number of command line arguments.
  sys.argv[0] is the name of the current Python script.
"""

# Get count of arguments
arg_count = len(sys.argv)
print("Count of arguments passed:", arg_count)

# Arguments passed
print("\nName of Python script:", sys.argv[0])

print("\nArguments passed:", end=" ")

for args_str in range(1, arg_count):
    print(sys.argv[args_str], end=" ")

# Addition of numbers
Sum = 0

# Using argparse module
for arg_str in range(1, arg_count):
    Sum += int(sys.argv[arg_str])

print("\n\nResult:", Sum)

