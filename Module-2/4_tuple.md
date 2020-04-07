
![](https://www.python.org/static/img/python-logo.png)

## Tuple
 - A tuple is an **immutable** sequence of Python objects 
 - Tuples are sequences, just like lists
 - The tuples cannot be changed unlike lists
 - Tuples use parentheses, whereas lists use square brackets.
 
    ```python
    tup_1 = ('Berlin', 'London', 2019, 2020)
    tup_2 = (1, 2, 3, 4, 5 )
    tup_3 = "a", "b", "c", "d"

    ```
 - The empty tuple is written as
    - tup_obj = ()
    
 - A single value tuple
    - tup_obj = (5,)
    
 - Accessing Values
    ```python
    
    tup_1 = ('Berlin', 'London', 2019, 2020)
    tup_2 = (1, 2, 3, 4, 5, 6, 7 )
    print("tup1[0]: ", tup_1[0])
    print("tup2[1:5]: ", tup_2[1:5])

    ```
 - Updating
    - Tuples are immutable which means you cannot update or change the values of tuple elements. 
    - You are able to take portions of existing tuples to **create new** tuples.
    
    ```python

       tup_1 = (12, 34.56)
       tup_2 = ('abc', 'xyz')

       # Following operation is invalid for tuples
       # tup_1[0] = 100

       # So let's create a new tuple as follows
       tup_3 = tup_1 + tup_2
       print(tup_3)

    ```
    
 - Delete Elements
    - Removing individual tuple elements is not possible. 

    ```python
       tup_obj = ('Berlin', 'London', 2019, 2020)
       print(tup_obj)
       del tup_obj
    ```    
    
 - Basic Operations
 
    |Expression|Results|Description|
    |-----------------|-------|-----------|
    |len((1, 2, 3))|3|Length|
    |(1, 2, 3) + (4, 5, 6)|(1, 2, 3, 4, 5, 6)|Concatenation|
    |('Hi!',) * 4|('Hi!', 'Hi!', 'Hi!', 'Hi!')|Repetition|
    |3 in (1, 2, 3)|True|Membership|
    |for x in (1, 2, 3): print(x)|1 2 3|Iteration|
 
 - Indexing, Slicing, Matrixes
 
     ```python
       tup_1 = ('Berlin', 'London', 2019, 2020)   
     ```
    |Expression|Results|Description|
    |-----------------|-------|-----------|
    |tup_1[2]|2019|Offsets start at zero|
    |tup_1[-2]|2019|Negative: count from the right|
    |tup_1[1:]|('London', 2019, 2020)|Slicing fetches sections|
 
 - Built-in Functions
 
    |Sr.No.|Function|Description|
    |------|-----------|---------------------|
    |1|cmp(tuple1, tuple2)|Compares elements of both tuples.|
    |2|len(tuple)|Gives the total length of the tuple.|
    |3|max(tuple)|Returns item from the tuple with max value.|
    |4|min(tuple)|Returns item from the tuple with min value.|
    |5|tuple(seq)|Converts a list into tuple.|
    

 [Example Script 22 - m2-script22.py](/Examples/Module-2/m2-script22.py)
#
[Main...](https://github.com/ptoraskar/Python-Learning/blob/master/README.md) | [Back...](/Module-2/3_list.md) | [Next...](/Module-2/5_dictionary.md)
