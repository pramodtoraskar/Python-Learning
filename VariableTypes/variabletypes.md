
# Variable Types
 Reserved memory locations to store values are nothing but Variables. This means that when you create a variable you reserve some space in memory.
 Based on the data type of a variable, the python interpreter allocates memory and decides what can be stored in the reserved memory. 

## Assigning Values to Variables
 In python variables do not need explicit declaration to reserve memory space. 
 The declaration happens automatically when you assign a value to a variable. The equal sign (=) is used to assign values to variables.
 The operand to the left of the = operator is the name of the variable and the operand to the right of the = operator is the value stored in the variable. 

 For example −
```python
#!/usr/bin/python

counter = 50          # An integer assignment
miles   = 100.0       # A floating point
name    = "python"    # A string

print counter
print miles
print name
```

## Multiple Assignment
 Python allows programmer to assign a single value to several variable simultaneously.

 For example - 
```python
   a = b = c = 4
```

 All three variables are assigned to the same memory location.
 You can also assign multiple objects to multiple variables 
 
 For example -
```python
   a, b, c = 1, 2, 'python'
```

## Standard Data Types
 Python has five standard data types -
 ..* Numbers
 ..* String
 ..* List
 ..* Tuple
 ..* Dictinoary
 
## Numbers
 Number objects are created when you assign a value to them. Number data types store numeric values 
 For example -
 
```python
   num1 = 5
   num2 = 10
```

 There are four different numerical data types - 
 ..* int ( single integers )
 ..* long ( Long integers have unlimited precision )
 ..* float ( floating points real values )
 ..* complex ( complex number have a real and imaginary part )
 
## Strings
 A contiguous set of characters reprsented in the quotation marks.
 Python program allows for either pairs of single '' or double "" quotes.
 
 Slice Operation:
 
 The slice operator ([] and [:]) with indexes starting at 0 in then beginning of the string
 In string reverse start from -1 
  
 For example - 
```python

   str_obj = "Hellow python!"
   
   print str_obj             # Prints entier string
   print str_obj[0]          # Prints first character of the string
   print str_obj[2:5]        # Prints characters starting from 3rd to 5th
   print str[2:]             # Prints string starting from 3rd character
   print str * 2             # Prints string two times
   print str + "Demo"        # Prints concatenated string
```
 
## Lists
 Python has a great built-in list type named "list". List literals are written within square brackets [ ]. 
 Lists work similarly to strings -- use the len() function and square brackets [ ] to access data, with the first element at index 0.
```python
  colors = ['red', 'blue', 'green']
  print colors[0]    ## red
  print colors[2]    ## green
  print len(colors)  ## 3
```

![alt text](../img/list1.png "Logo Title Text 1")

Assignment with an = on lists does not make a copy. Instead, assignment makes the two variables point to the one list in memory.

```python
   b = colors   ## Does not copy the list
```

![alt text](../img/list2.png "Logo Title Text 1")

The "empty list" is just an empty pair of brackets [ ]. The '+' works to append two lists, so [1, 2] + [3, 4] yields [1, 2, 3, 4] (this is just like + with strings).

#### FOR and IN
 Python's *for* and *in* constructs are extremely useful, and the first use of them we'll see is with lists. The *for* construct -- for var in list -- is an easy way to look at each element in a list (or other collection). Do not add or remove from the list during iteration.
```python
  squares = [1, 4, 9, 16]
  sum = 0
  for num in squares:
    sum += num
  print sum  ## 30
```

If you know what sort of thing is in the list, use a variable name in the loop that captures that information such as "num", or "name", or "url". Since python code does not have other syntax to remind you of types, your variable names are a key way for you to keep straight what is going on.

The *in* construct on its own is an easy way to test if an element appears in a list (or other collection) -- value in collection -- tests if the value is in the collection, returning True/False.

```python
  list = ['larry', 'curly', 'moe']
  if 'curly' in list:
    print 'yay'
```
The for/in constructs are very commonly used in Python code and work on data types other than list, so you should just memorize their syntax. You may have habits from other languages where you start manually iterating over a collection, where in Python you should just use for/in.

You can also use for/in to work on a string. The string acts like a list of its chars, so for ch in s: print ch prints all the chars in a string.

#### Range

The range(n) function yields the numbers 0, 1, ... n-1, and range(a, b) returns a, a+1, ... b-1 -- up to but not including the last number. The combination of the for-loop and the range() function allow you to build a traditional numeric for loop:
```python
  ## print the numbers from 0 through 99
  for i in range(100):
    print i
There is a variant xrange() which avoids the cost of building the whole list for performance sensitive cases (in Python 3000, range() will have the good performance behavior and you can forget about xrange()).
```

While Loop

Python also has the standard while-loop, and the *break* and *continue* statements work as in C++ and Java, altering the course of the innermost loop. The above for/in loops solves the common case of iterating over every element in a list, but the while loop gives you total control over the index numbers. Here's a while loop which accesses every 3rd element in a list:

```python
  ## Access every 3rd element in a list
  i = 0
  while i < len(a):
    print a[i]
    i = i + 3
```

#### List Methods

Here are some other common list methods.

list.append(elem) -- adds a single element to the end of the list. Common error: does not return the new list, just modifies the original.
list.insert(index, elem) -- inserts the element at the given index, shifting elements to the right.
list.extend(list2) adds the elements in list2 to the end of the list. Using + or += on a list is similar to using extend().
list.index(elem) -- searches for the given element from the start of the list and returns its index. Throws a ValueError if the element does not appear (use "in" to check without a ValueError).
list.remove(elem) -- searches for the first instance of the given element and removes it (throws ValueError if not present)
list.sort() -- sorts the list in place (does not return it). (The sorted() function shown below is preferred.)
list.reverse() -- reverses the list in place (does not return it)
list.pop(index) -- removes and returns the element at the given index. Returns the rightmost element if index is omitted (roughly the opposite of append()).
Notice that these are *methods* on a list object, while len() is a function that takes the list (or string or whatever) as an argument.

```python
  list = ['larry', 'curly', 'moe']
  list.append('shemp')         ## append elem at end
  list.insert(0, 'xxx')        ## insert elem at index 0
  list.extend(['yyy', 'zzz'])  ## add list of elems at end
  print list  ## ['xxx', 'larry', 'curly', 'moe', 'shemp', 'yyy', 'zzz']
  print list.index('curly')    ## 2

  list.remove('curly')         ## search and remove that element
  list.pop(1)                  ## removes and returns 'larry'
  print list  ## ['xxx', 'moe', 'shemp', 'yyy', 'zzz']

Common error: note that the above methods do not *return* the modified list, they just modify the original list.

  list = [1, 2, 3]
  print list.append(4)   ## NO, does not work, append() returns None
  ## Correct pattern:
  list.append(4)
  print list  ## [1, 2, 3, 4]
```

#### List Build Up

One common pattern is to start a list a the empty list [], then use append() or extend() to add elements to it:

```python
  list = []          ## Start as the empty list
  list.append('a')   ## Use append() to add elements
  list.append('b')
````

##### List Slices

Slices work on lists just as with strings, and can also be used to change sub-parts of the list.

```python
  list = ['a', 'b', 'c', 'd']
  print list[1:-1]   ## ['b', 'c']
  list[0:2] = 'z'    ## replace ['a', 'b'] with ['z']
  print list         ## ['z', 'c', 'd']
```

**Exercise:**
 
```python
    m=[[0]*3]*2
    for i in range(3):
        m[0][i]=1
    
    print m
```

## Tuples
 A tuple is a sequence of immutable Python objects. Tuples are sequences, just like lists. The differences between tuples and lists are, the tuples cannot be changed unlike lists and tuples use parentheses, whereas lists use square brackets.
 Creating a tuple is as simple as putting different comma-separated values. Optionally you can put these comma-separated values between parentheses also. For example −
```python
   tup1 = ('technology', 'cloud', 2.0, 2020);
   tup2 = (1, 2, 3, 4, 5 );
   tup3 = "a", "b", "c", "d";
``` 
 The empty tuple is written as two parentheses containing nothing −
 
```python
    tup1 = ();
```
 To write a tuple containing a single value you have to include a comma, even though there is only one value −
```python
    tup1 = (5,);
```

 It's a funny case in the syntax, but the comma is necessary to distinguish the tuple from the ordinary case of putting an expression in parentheses. In some cases you can omit the parenthesis and Python will see from the commas that you intend a tuple.

 Assigning a tuple to an identically sized tuple of variable names assigns all the corresponding values. If the tuples are not the same size, it throws an error. This feature works for lists too.
```python
  (x, y, z) = (42, 13, "hike")
  print z  ## hike
  (err_string, err_code) = Foo()  ## Foo() returns a length-2 tuple
```

## Dictionary ==  Dict Hash Table

Python's efficient key/value hash table structure is called a "dict". The contents of a dict can be written as a series of key:value pairs within braces { }, e.g. dict = {key1:value1, key2:value2, ... }. The "empty dict" is just an empty pair of curly braces {}.

Looking up or setting a value in a dict uses square brackets, e.g. dict['foo'] looks up the value under the key 'foo'. Strings, numbers, and tuples work as keys, and any type can be a value. Other types may or may not work correctly as keys (strings and tuples work cleanly since they are immutable). Looking up a value which is not in the dict throws a KeyError -- use "in" to check if the key is in the dict, or use dict.get(key) which returns the value or None if the key is not present (or get(key, not-found) allows you to specify what value to return in the not-found case).
```python
  ## Can build up a dict by starting with the the empty dict {}
  ## and storing key/value pairs into the dict like this:
  ## dict[key] = value-for-that-key
  dict = {}
  dict['a'] = 'alpha'
  dict['g'] = 'gamma'
  dict['o'] = 'omega'

  print dict  ## {'a': 'alpha', 'o': 'omega', 'g': 'gamma'}

  print dict['a']     ## Simple lookup, returns 'alpha'
  dict['a'] = 6       ## Put new key/value into dict
  'a' in dict         ## True
  ## print dict['z']                  ## Throws KeyError
  if 'z' in dict: print dict['z']     ## Avoid KeyError
  print dict.get('z')  ## None (instead of KeyError)
```

![alt text](https://github.com/ptoraskar/Python-Learning/blob/master/img/dict.png "Logo Title Text 1")

 A for loop on a dictionary iterates over its keys by default. The keys will appear in an arbitrary order. The methods dict.keys() and dict.values() return lists of the keys or values explicitly. There's also an items() which returns a list of (key, value) tuples, which is the most efficient way to examine all the key value data in the dictionary. All of these lists can be passed to the sorted() function.
```python
  ## By default, iterating over a dict iterates over its keys.
  ## Note that the keys are in a random order.
  for key in dict: print key
  ## prints a g o
  
  ## Exactly the same as above
  for key in dict.keys(): print key

  ## Get the .keys() list:
  print dict.keys()  ## ['a', 'o', 'g']

  ## Likewise, there's a .values() list of values
  print dict.values()  ## ['alpha', 'omega', 'gamma']

  ## Common case -- loop over the keys in sorted order,
  ## accessing each key/value
  for key in sorted(dict.keys()):
    print key, dict[key]
  
  ## .items() is the dict expressed as (key, value) tuples
  print dict.items()  ##  [('a', 'alpha'), ('o', 'omega'), ('g', 'gamma')]

  ## This loop syntax accesses the whole dict by looping
  ## over the .items() tuple list, accessing one (key, value)
  ## pair on each iteration.
  for k, v in dict.items(): print k, '>', v
  ## a > alpha    o > omega     g > gamma
```

 There are "iter" variants of these methods called iterkeys(), itervalues() and iteritems() which avoid the cost of constructing the whole list -- a performance win if the data is huge. However, I generally prefer the plain keys() and values() methods with their sensible names. In Python 3000 revision, the need for the iterkeys() variants is going away.

 Strategy note: from a performance point of view, the dictionary is one of your greatest tools, and you should use it where you can as an easy way to organize data. For example, you might read a log file where each line begins with an IP address, and store the data into a dict using the IP address as the key, and the list of lines where it appears as the value. Once you've read in the whole file, you can look up any IP address and instantly see its list of lines. The dictionary takes in scattered data and makes it into something coherent.

####Dict Formatting

 The % operator works conveniently to substitute values from a dict into a string by name:
```python
  hash = {}
  hash['word'] = 'garfield'
  hash['count'] = 42
  s = 'I want %(count)d copies of %(word)s' % hash  # %d for int, %s for string
  # 'I want 42 copies of garfield'
```
 **Del**

 The "del" operator does deletions. In the simplest case, it can remove the definition of a variable, as if that variable had not been defined. Del can also be used on list elements or slices to delete that part of the list and to delete entries from a dictionary.
```python
  var = 6
  del var  # var no more!
  
  list = ['a', 'b', 'c', 'd']
  del list[0]     ## Delete first element
  del list[-2:]   ## Delete last two elements
  print list      ## ['b']

  dict = {'a':1, 'b':2, 'c':3}
  del dict['b']   ## Delete 'b' entry
  print dict      ## {'a':1, 'c':3}
```  


## Data Type Conversion
 There are several built-in functions to perform conversion from one data type to another. These functions return a new object representing the converted value.
 
 |    Function	         |                                 Description                            |
 | --------------------  |:----------------------------------------------------------------------:|
 | int(x [,base])        | Converts x to an integer. base specifies the base if x is a string.    |
 | long(x [,base] )      | Converts x to a long integer. base specifies the base if x is a string.|
 | float(x)              | Converts x to a floating-point number.                                 |
 | complex(real [,imag]) | Creates a complex number.                                              |
 | str(x)                | Converts object x to a string representation.                          |
 | repr(x)               | Converts object x to an expression string.                             |
 | eval(str)             | Evaluates a string and returns an object.                              |
 | tuple(s)              | Converts s to a tuple.                                                 |
 | list(s)               | Converts s to a list.                                                  |
 | set(s)                | Converts s to a set.                                                   |
 | dict(d)               | Creates a dictionary. d must be a sequence of (key,value) tuples.      |
 | frozenset(s)          | Converts s to a frozen set.                                            |
 | chr(x)                | Converts an integer to a character.                                    |
 | unichr(x)             | Converts an integer to a Unicode character.                            |
 | ord(x)                | Converts a single character to its integer value.                      |
 | hex(x)                | Converts an integer to a hexadecimal string.                           |
 | oct(x)                | Converts an integer to an octal string.                                |

## List Comprehensions (optional)

 List comprehensions are a more advanced feature which is nice for some cases but is not needed for the exercises and is not something you need to learn at first (i.e. you can skip this section). A list comprehension is a compact way to write an expression that expands to a whole list. Suppose we have a list nums [1, 2, 3], here is the list comprehension to compute a list of their squares [1, 4, 9]:
```python
  nums = [1, 2, 3, 4]

  squares = [ n * n for n in nums ]   ## [1, 4, 9, 16]
```  
 The syntax is [ expr for var in list ] -- the for var in list looks like a regular for-loop, but without the colon (:). The expr to its left is evaluated once for each element to give the values for the new list. Here is an example with strings, where each string is changed to upper case with '!!!' appended:
```python
  strs = ['hello', 'and', 'goodbye']

  shouting = [ s.upper() + '!!!' for s in strs ]
  ## ['HELLO!!!', 'AND!!!', 'GOODBYE!!!']
```
 You can add an if test to the right of the for-loop to narrow the result. The if test is evaluated for each element, including only the elements where the test is true.
```python
  ## Select values <= 2
  nums = [2, 8, 1, 6]
  small = [ n for n in nums if n <= 2 ]  ## [2, 1]

  ## Select fruits containing 'a', change to upper case
  fruits = ['apple', 'cherry', 'bannana', 'lemon']
  afruits = [ s.upper() for s in fruits if 'a' in s ]
  ## ['APPLE', 'BANNANA']
```