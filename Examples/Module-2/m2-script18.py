
# Python code to illustrate read() mode
fp_obj = open("python_learning.text", "r")
print(fp_obj.read())
fp_obj.close()


# Python code to illustrate read() mode character wise
fp_obj = open("python_learning.txt", "r")
print(fp_obj.read(5))
fp_obj.close()


# Python code to create a file
fp_obj = open('python_learning_test.txt', 'w')
fp_obj.write("This is the write command test")
fp_obj.write("It allows us to write in a particular test file")
fp_obj.close()
