# How to Install Python on Windows

You will need to open up your browser and go to the [Python download page](https://www.python.org/downloads/windows/).

Now that you are on the download page, select which of the software builds you would like to download. 
For the purposes of this article we will use the most up to date version available (Python 2.7.12).

Once you have clicked on that, you will be taken to a page with a description of all the new updates and features of 2.7.12, however, you can always read that while the download is in process. 
Scroll to the bottom of the page till you find the “Download” section and click on the link that says “download page.”

Now you will scroll all the way to the bottom of the page and find the “Windows x86 MSI installer.” If you want to download the 86-64 bit MSI, feel free to do so. 

#### Installing Python
Once you have downloaded the Python MSI, simply navigate to the download location on your computer, double clicking the file and pressing Run when the dialog box pops up.

If you are the only person who uses your computer, simply leave the “Install for all users” option selected. 
If you have multiple accounts on your PC and don’t want to install it across all accounts, select the “Install just for me” option then press “Next.”

If you want to change the install location, feel free to do so; however, it is best to leave it as is and simply select next.

Scroll down in the window and find the “Add Python.exe to Path” and click on the small red “x.” Choose the “Will be installed on local hard drive” option then press “Next.”

You will notice that the installation will bring up a command prompt window while Python downloads and installs ["Pip."](https://pypi.python.org/pypi) Pip is just a package management tool. 
This will allow you to install all the additional Python packages that are available for download through PyPI (Python Package Index).

Now that you have completed the installation process, click on “Finish.”

#### Adding Python to System Path Variable

Once you have successfully installed Python, it is time to add it to the System Path Variable. Doing this will allow Python to run scripts on your computer without any conflicts of problems.

Begin by opening the start menu and typing in “environment” and select the option called “Edit the system environment variables.”

When the “System Properties” window appears, click on “Environment Variables…”

Once you have the “Environment Variables” window open, direct your focus to the bottom half. 
You will notice that it controls all the “System Variables” rather than just this associated with your user. Click on “New…” to create a new variable for Python.

Simply enter a name for your Path and the code shown below. For the purposes of this example we have installed Python 2.7.12, so we will call the path: "Pythonpath."

The string that you will need to enter is: “C:\Python27\;C:\Python27\Scripts;”

Press “OK,” then “OK,” then “OK,” then the red “X” to accept all changes and exit the “System Properties” window.


###### You have successfully installed Python, added the environment variables. Congratulations. If you would like to learn more about Python scripting.




