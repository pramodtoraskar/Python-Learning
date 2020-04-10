 
![](https://www.python.org/static/img/python-logo.png)

## Modules and Packages

#### Modules
 - A module allows you to logically organize your Python code
 - Grouping related code into a module makes the code easier to understand and use
 - A module is a file consisting of Python code. 
 - A module can define functions, classes and variables. 
 - A module can also include runnable code 
 - The Python code for a module named **aname** normally resides in a file named **aname.py**. 
 - A simple module, **supportsys.py**  
   
   ```python
       import sys
    
       def print_py_version_func():
           if not sys.version_info.major == 3 and sys.version_info.minor >= 6:
           print("Python 3.6 or higher is required.")
           print("You are using Python {}.{}.".format(sys.version_info.major, sys.version_info.minor))
           sys.exit(1)
    ```
 
 - The import Statement
   - You can use any Python source file as a module by executing an import statement in some other Python source file
     > import module1[, module2[,... moduleN]
   
     ```python
        # Import module support
        import supportsys

        # Now you can call defined function that module as follows
        supportsys.print_py_version_func()
     ```
   - Python's **from** statement lets you import specific attributes from a module into the current namespace
     > from modulename import name1[, name2[, ... nameN]]
     ```python
        from supportsys import print_py_version_func

        print_py_version_func()
     ```
   - To import all names from a module into the current namespace by.
     > from modname import *
     
 - Locating Modules  
    - When you import a module, the Python interpreter searches for the module 
    - in the following sequences
        - The current directory.
        - Then searches each directory in the shell variable PYTHONPATH
        - Python checks the default path
            > In Unix/Linux */usr/local/lib/python/*
 
#### Packages
  - Packages in Python
    - A package is a hierarchical file directory structure 
    - That defines a single Python application environment that consists of modules and subpackages and sub-subpackages
    
    - To create this project locally, create the following file structure:
    ```html
       packaging_tutorial/
           example_pkg/
               __init__.py
    ```
 - Creating the package files
    - You will now create a handful of files to package up this project and prepare it for distribution
    ```html
       packaging_tutorial/
          example_pkg/
            __init__.py
          tests/
          setup.py
          LICENSE
          README.md
    ```
    - Creating a test folder
        - **tests/** is a placeholder for unit test files
    - Creating setup.py
        - setup.py is the build script for setuptools. 
        - It tells setuptools about your package (such as the name and version) as well as which code files to include.
        ```python
            import setuptools
    
            with open("README.md", "r") as fh:
                long_description = fh.read()
            
            setuptools.setup(
                name="Pramod Toraskar", # Replace with your own username
                version="0.0.1",
                author="Example Author",
                author_email="ptoraska@redhat.com",
                description="A small example package",
                long_description=long_description,
                long_description_content_type="text/markdown",
                url="https://github.com/ptoraskar/Python-Learning",
                packages=setuptools.find_packages(),
                classifiers=[
                    "Programming Language :: Python :: 3",
                    "License :: OSI Approved :: MIT License",
                    "Operating System :: OS Independent",
                ],
                python_requires='>=3.6',
            )
        ```
        - Creating README.md
            - Open README.md and enter the following content
        - Creating a LICENSE        
 - Generating distribution archives
    - The next step is to generate distribution packages for the package
    - These are archives that are uploaded to the Package Index and can be installed by pip.
    - Make sure you have the latest versions of setuptools and wheel installed
        ```bash
          python3 -m pip install --user --upgrade setuptools wheel
        ```
    - Now run this command from the same directory where setup.py is located
        ```bash
          python3 setup.py sdist bdist_wheel
        ```
    - This command should output a lot of text and once completed should generate two files in the dist directory
        ```html
            dist/
              example_pkg_YOUR_USERNAME_HERE-0.0.1-py3-none-any.whl
              example_pkg_YOUR_USERNAME_HERE-0.0.1.tar.gz
        ```
 - Uploading the distribution archives
    - Finally, it’s time to upload your package to the Python Package Index [pypi]
    - Need to verify your email address before you’re able to upload any packages
    - Create a PyPI API token so you will be able to securely upload your project
    - Go to **https://test.pypi.org/manage/account/#api-tokens** and create a new API token
    - You can use [twine](https://packaging.python.org/key_projects/#twine) to upload the distribution packages
        ```bash
           python3 -m pip install --user --upgrade twine
        ```
    - Once installed, run Twine to upload all of the archives under dist
        ```bash
           python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
        ```
    - You will be prompted for a username and password. 
        - For the username, use __token__. 
        - For the password, use the token value, including the pypi- prefix    

    - After the command completes, you should see output similar to this:
        ```bash
            Uploading distributions to https://test.pypi.org/legacy/
            Enter your username: [your username]
            Enter your password:
            Uploading example_pkg_YOUR_USERNAME_HERE-0.0.1-py3-none-any.whl
            100%|█████████████████████| 4.65k/4.65k [00:01<00:00, 2.88kB/s]
            Uploading example_pkg_YOUR_USERNAME_HERE-0.0.1.tar.gz
            100%|█████████████████████| 4.25k/4.25k [00:01<00:00, 3.05kB/s]
        ```
    - Installing your newly uploaded package
        ```bash
          python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps example-pkg-YOUR-USERNAME-HERE
        ```        
#   
[Main...](https://github.com/ptoraskar/Python-Learning/blob/master/README.md) | [Next...](/Module-3/2_functions.md)