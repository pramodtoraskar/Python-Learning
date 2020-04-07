
![](https://www.python.org/static/img/python-logo.png)


## Files I/O Functions

- We know how reading and writing to the standard input and output. 
- Now, we will see how to use actual data files.

  - open() mode
  
    - open () function in Python to open a file in read or write mode
    - open () will return a file object
    - To return a file object we use open() function along with two arguments, that accepts file name and the mode, whether to read or write.
  
    - mode's
      - “ r “, for reading.
      - “ w “, for writing.
      - “ a “, for appending.
      - “ r+ “, for both reading and writing
  
      ```python
    
         # A file named "python_learning", will be opened with the reading mode.
         fp_obj = open('python_learning.txt', 'r') 
        
         # This will print every line one by one in the file 
         for each in fp_obj:
             print (each)
      ```
      [Example Script 17 - m2-script17.py](/Examples/Module-2/m2-script17.py)
  
    - The file Object Attributes
      - *file.closed* - Returns true if file is closed, false otherwise.
      - *file.mode*   - Returns access mode with which file was opened.
      - *file.name*   - Returns name of the file.
    
  - read() mode
  
    - If you need to extract a string that contains all characters in the file then we can use file.read()
    - Pointer tries to read as much as possible, maybe until the end of file.
        ```python
        
            # Python code to illustrate read() mode 
            fp_obj = open("python_learning.text", "r") 
            print(fp_obj.read())
        ```
  
    - To read a file is to call a certain number of characters like in the following code the interpreter will 
      read the first five characters of stored data and return it as a string.  
        ```python
          # Python code to illustrate read() mode character wise 
          fp_obj = open("python_learning.txt", "r") 
          print(fp_obj.read(5))
        ```
  - write() mode
  
    - Creating a file using write() mode
    - how to create a file and how write mode 
      ```python
          # Python code to create a file
          fp_obj = open('python_learning_test.txt','w')
          fp_obj.write("This is the write command test") 
          fp_obj.write("It allows us to write in a particular test file") 
          fp_obj.close()
      ```
      [Example Script 18 - m2-script18.py](/Examples/Module-2/m2-script18.py)

  - append() mode
  
    - The append mode works
      ```python
         # Python code to illustrate append() mode
         fp_obj = open('python_learning_test.txt','a')
         fp_obj.write("This will add this line")
         fp_obj.close()
      ```
      [Example Script 19 - m2-script19.py](/Examples/Module-2/m2-script19.py)
  
  *Note*: other commands in file handling that is useful
  
  - rstrip(): strips each line of a file off spaces from the right-hand side.
  - lstrip(): strips each line of a file off spaces from the left-hand side.
  
  - with():
  
    - This is helpful because using this method any files opened will be closed automatically after one is done, 
      so auto-cleanup.
    ```python
      # Python code to illustrate with()

      from pprint import pprint

      with open("python_learning_test.txt") as fp_obj: 
          data = fp_obj.read()
          # do something with data
          pprint(data) 
    ```
  
    Let illustrate with() along with write()
  
    ```python
       # Python code to illustrate with() along with write() 
       with open("python_learning_new.txt", "w") as fp_obj:
          fp_obj.write("This new Python learning!!!")
     ```

  - split()

    - This splits the variable when space is encountered. 
    - You can also split using any characters as we wish. 

    ```python
        # Python code to illustrate split() function 
        with open("python_learning_new.txt", "r") as fp_obj:
            data = fp_obj.readlines()
            for line in data:
                word = line.split()
                print(word)
    ```
    [Example Script 20 - m2-script20.py](/Examples/Module-2/m2-script20.py)


  - close() mode
  
    - The close() command terminates all the resources in use and frees the system of this particular program.

    ```python
        # Open a file
        fp_obj = open("python_learning_new.txt", "wb")
        print("Name of the file: ", fp_obj.name)
        
        # Close opened file
        fp_obj.close()
    ```

#
[Main...](https://github.com/ptoraskar/Python-Learning/blob/master/README.md) | [Next...](/Module-2/2_numbers_strings_functions.md)



