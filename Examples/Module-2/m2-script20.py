
from pprint import pprint

# Python code to illustrate with()
with open("python_learning_test.txt") as fp_obj:
    data = fp_obj.read()
    # do something with data
    pprint(data)


# Python code to illustrate with() along with write()
with open("python_learning_new.txt", "w") as fp_obj:
    fp_obj.write("This new Python learning!!!")


# Python code to illustrate split() function
with open("python_learning_new.text", "r") as fp_obj:
    data = fp_obj.readlines()
    for line in data:
        word = line.split()
        print(word)


# Open a file
fp_obj = open("python_learning_new.txt", "wb")
print("Name of the file: ", fp_obj.name)

# Close opened file
fp_obj.close()