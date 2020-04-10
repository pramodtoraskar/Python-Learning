 
![](https://www.python.org/static/img/python-logo.png)

## Installing Packages

 - How to install Python packages.
    - Ensure you can run Python from the command line
        > python --version
    - Ensure you can run pip from the command line
        > pip --version
    - Ensure pip, setuptools, and wheel are up to date
        > python -m pip install --upgrade pip setuptools wheel
        
    - Optionally, create a virtual environment ( Recommended )
        - There are two common tools for creating Python virtual environments
            - **venv** is available by default in Python 3.3 and later, and installs pip and setuptools    
                > python3 -m venv tutorial_env <br/>
                  source tutorial_env/bin/activate
            - **virtualenv** needs to be installed separately
    
    - **Note**: Go to the [pypi](https://pypi.org/) and search package
     
    - Installing from PyPI
        ```bash
          pip install "SomeProject"
          
          pip install notebook
    
          jupyter notebook
        ```
    - To install a specific version
        ```bash
         # To install a specific version
         pip install "notebook==6.0.3"
         # To install greater than or equal
         pip install "notebook>=6.0.1,<6.0.3"
        ```
 - Requirements files
 
    - Install a list of requirements specified in a **Requirements** File.
    ```bash
       pip install -r requirements.txt
    ```
- Uninstalling Packages¶
    - To list installed packages:
      > pip list
    ```bash
       pip uninstall notebook
    ```
  
#
[Main...](https://github.com/ptoraskar/Python-Learning/blob/master/README.md) | [Back...](/Module-3/8_Modules_and_Packages.md)