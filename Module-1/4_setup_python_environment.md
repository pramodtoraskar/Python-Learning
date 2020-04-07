
![](https://www.python.org/static/img/python-logo.png)

 
## Setup Python Environment

- Python is available on a wide variety of platforms including Linux and Mac OS X.
- Open a terminal window and type "python" to find out if it is already installed 
- You need to download only the binary code applicable for your platform and install Python.

> Open a Web browser and go to [https://www.python.org/downloads](https://www.python.org/downloads/) as per platform.

- Unix and Linux Installation
    - Open a Web browser and go to [https://www.python.org/downloads/](https://www.python.org/downloads/).
    - Follow the link to download zipped source code available for Unix/Linux.
    - Download and extract files. (home directory `/home/<usernale>/`)
    - Go to the extracted directory and execute.
    - run ./configure script
    - make
    - make install
    
    ```
    This installs Python at standard location /usr/local/bin and its libraries at 
      /usr/local/lib/pythonXX where XX is the version of Python.
    ```
    
- Windows Installation
    - Run the Python Installer from downloads folder. 
    - Make sure to mark Add Python 3.7 to PATH otherwise you will have to do it explicitly.
    
    ![](/img/python-install-windows-1.png)
    
    It will start installing python on windows.

- Setting path at Unix/Linux

    - To add the Python directory to the path for a particular session in Unix −
        - In the csh shell − type and press Enter. 
        ```bash
        setenv PATH "$PATH:/usr/local/bin/python"
        ```        
    - In the bash shell (Linux) − type and press Enter.
        ```bash
        export PATH="$PATH:/usr/local/bin/python"
        ```
   
    - In the sh or ksh shell − type and press Enter.
    ```bash
       PATH="$PATH:/usr/local/bin/python"
    ```
    
    - Note − /usr/local/bin/python is the path of the Python directory

- Setting path at Windows
    - To add the Python directory to the path for a particular session in Windows −
       - At the command prompt − type and press Enter.
       ```bash
       path %path%;C:\Python
      ```
    - Note − C:\Python is the path of the Python directory

- Python Environment Variables

    - *PYTHONPATH*
        - It has a role similar to PATH. This variable tells the Python interpreter where to locate the module files
        imported into a program
    - *PYTHONSTARTUP*
        - It contains the path of an initialization file containing Python source code.
    - *PYTHONCASEOK*
        - It is used in Windows to instruct Python to find the first case-insensitive match in an import statement.
    - *PYTHONHOME*
        - It is an alternative module search path.


## Discuss Python Scripts on Unix/Window

- Running Python

    - Interactive Interpreter
      - Enter python the command line.
      
          ```bash     
                $ python # Unix/Linux
                or
                python% # Unix/Linux
                or
                C:> python # Windows/DOS
            ```
      -  The available command line options
        
            |   |Option|Description                                                                                 |
            |---|------|--------------------------------------------------------------------------------------------|   
            |1	|-d	|It provides debug output.                                                                      |
            |2	|-O	|It generates optimized bytecode (resulting in .pyo files).                                     |
            |3	|-S	|Do not run import site to look for Python paths on startup.                                    |
            |4	|-v	|verbose output (detailed trace on import statements).                                          |
            |5	|-X	|disable class-based built-in exceptions (just use strings); obsolete starting with version 1.6.|
            |6	|-c	|cmd  run Python script sent in as cmd string                                                   |
            |7	|file |run Python script from given file                                                            |
            
      - Let's try Interactive Interpreter
    
        ```python
           print("Hello")
        ```
        [Example Script 1: m1-script1.py](/Examples/Module-1/m1-script1.py)
    
    - Script from the Command-line
    
      - A Python script can be executed at command line by invoking the interpreter on your script

        ```bash

            $ python m1-script1.py# Unix/Linux
            
            or

            python% m1-script1.py # Unix/Linux

            or 

            C:> python m1-script1.py # Windows/DOS     
        ```      
   
## Basic Syntax
 
- Python Identifiers
    - Python is a case sensitive programming language. 
      - Thus, **Pandemic** and **pandemic** are two different identifiers in Python.

- Reserved Words
    - *and*, *break*, *del*, *lambda*, *is*

- Lines and Indentation

- Multi-Line Statements

- Quotation in Python

    ```html
    word = 'RedHat'
    sentence = "This is a Open-source Company."
    paragraph = """This is a Open-source Company. Founded in 1993, 
                   Red Hat has its corporate headquarters in Raleigh, North Carolina, 
                   with other offices worldwide. It became a subsidiary of IBM on July 9, 2019."""
    ```
- Comments

#
[Main...](https://github.com/ptoraskar/Python-Learning/blob/master/README.md) | [Back...](/Module-1/3_popularity_and_applications.md) | [Next...](/Module-1/5_variables_to_expressions.md)


