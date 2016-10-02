# Python-Learning

 Discovering and learning the Python Programming -- personal notes.

## Introduction 

 Python is a general-purpose [ interpreted ](../master/interpreted-language.md), interactive, [ object-oriented ](../master/object-oriented.md) and high-level programming language.
 It was created by [ Guido Van Rossum ](https://en.wikipedia.org/wiki/Guido_van_Rossum) during 1985-1990. Python source code is also available under the GNU General Public License (GPL).
 
## Why learn Python?

 Python is a versatile and popular programming language. It's great as a first language because it is concise and easy to read, and it is also a good language to have in any programmer's 
 stack as it can be used for everything from web development to software development and scientific applications. 

## Prerequisites

 1. Installing Python
.. Installing Python is generally easy, and most of the time many Linux and UNIX distributions include a recent Python. 
.. If you do need to install Python and aren't confident about the task you can find a few notes on the [Windows-link](../master/windows-installation.md). 

 2. Open a GIT account - Link to GIT repo [site](https://github.com/) ** Optional

## Execute Python Programs

 Interactive Mode Programming

 Call the interpreter without passing a script file as a parameter brings up the following prompt −

```
$ python
```
 
 Type the following text at the Python prompt and press the Enter:

```python
>>> print ("Hello, Python!")
```

 Script Mode Programming

 Call the interpreter with a script parameter begins execution of the script and continues until the script is finished. When the script is finished, the interpreter is no longer active.

```python
#!/usr/bin/python

print "Hello, Python!"
```

## Identifiers

 Is a name used to identify a variable, function, class, module or other object in python.
 Identifiers starts with a letter A to Z or a to z or an underscore (_) followed by zero or more letters, underscores and digits (0 to 9).
 
 Python does not allow punctuation characters such as @, $, and % within identifiers. Python is a case sensitive programming language.
 
 **Talk** and **talk** are two different identifiers in Python.
 
 Naming conventions for Python identifiers
 
 ..* Class names start with an uppercase letter. All other identifiers start with a lowercase letter.
 ..* Private Identifier - Starting an identifier with a single leading underscore indicates that the identifier is private.

```python
     >>> _macwork
```
 ..* Strongly Private Identifier - with two leading underscores
```python
     >>> __macorgwork
```
 ..* If the identifier also ends with two trailing underscores, the identifier is a language-defined special name.
 
```
     >>> __init__
```

## Lines and Indentation
 Like other programming language python doesn't use braces '{}' to locate blocks of code for class or function definitions or flow control.
 Block of code are identify by line of indentation.
  
 The number of spaces in the indentation is variable, but all statements within the block must be indented the same amount.
  
 ex.
  
```python
   if True:
       print ("True")
   else:
       print ("False")
``` 

## Quotation
 Python programming language accepts single ('), double (") and triple (''' or """) quotes to denote string literals, as long as the same type of quote starts and ends the string.
 
 The triple quotes are used to span the string across multiple lines. 

```Python
   word = 'word'
   sentence = "This is a sentence."
   paragraph = """This is a paragraph. It is
   made up of multiple lines and sentences."""
```
 
## Comments
 A hash sign (#) - All characters after the # and up to the end of the physical line are part of the comment and the Python interpreter ignores them.
 
## User Input
  Below lines of the program displays the prompt the statement saying “Press the enter key to exit”, and waits for the user to take action −
  
```python
#!/usr/bin/python

input("Enter the key to exit.")
```

Here, We have completed basic system and python programming introductions. Let's see with more detailed syntax and python programming concepts. 
**So Let's start with python [Variable Types](../master/VariableTypes/variabletypes.md)**