
![](https://www.python.org/static/img/python-logo.png)

## List

 - The list is a most versatile data type available in Python which can be written as a list of comma-separated values 
   (items) between square brackets. 
 - Important thing about a list is that items in a list need not be of the same type.

    ```python
        list_1 = ['Berlin', 'London', 2019, 2020]
        list_2 = [1, 2, 3, 4, 5 ];
        list_3 = ["a", "b", "c", "d"] 
    ```
    
 - Accessing Values

    ```python
       list_1 = ['Berlin', 'London', 2019, 2020]
       list_2 = [1, 2, 3, 4, 5, 6, 7 ]
    
       print("list1[0]: ", list_1[0])
       print("list2[1:5]: ", list_2[1:5])

    ```
 - Updating
    
    ```python
       list_obj = ['Berlin', 'London', 2019, 2020]

       print("Value available at index 2 : ")
       
       print(list_obj[2])
       list_obj[2] = 2021;
       
       print("New value available at index 2 : ")
       print(list_obj[2])
    ```
 - Delete Elements
    ```python

       list_1 = ['Berlin', 'London', 2019, 2020]

       del list_1[2]

       print("After deleting value at index 2 : ")   

       print(list_1)

    ```
 - Basic Operations
 
    |Expression|Results|Description|
    |-----------------|-------|-----------|
    |len([1, 2, 3])|3|Length|
    |[1, 2, 3] + [4, 5, 6]|[1, 2, 3, 4, 5, 6]|Concatenation|
    |['Hi!'] * 4|['Hi!', 'Hi!', 'Hi!', 'Hi!']|Repetition|
    |3 in [1, 2, 3]|True|Membership|
    |for x in [1, 2, 3]: print(x)|1 2 3|Iteration|

 - Indexing, Slicing, Matrixes
    
    ```python
       list_1 = ['Berlin', 'London', 2019, 2020]   
    ```
    |Expression|Results|Description|
    |-----------------|-------|-----------|
    |list_1[2]|2019|Offsets start at zero|
    |list_1[-2]|2019|Negative: count from the right|
    |list_1[1:]|['London', 2019, 2020]|Slicing fetches sections|

 - Built-in Functions & Methods
 
    |Sr.No.|Function|Description|
    |------|--------|-----------|
    |1|cmp(list1, list2)|Compares elements of both lists.|
    |2|len(list)|Gives the total length of the list.|
    |3|max(list)|Returns item from the list with max value.|
    |4|min(list)|Returns item from the list with min value.|
    |5|list(seq)|Converts a tuple into list.|

    - Python includes following list methods

    |Sr.No.|Methods|Description|
    |------|--------|-----------|
    |1|list.append(obj)|Appends object obj to list|
    |2|list.count(obj)|Returns count of how many times obj occurs in list|
    |3|list.extend(seq)|Appends the contents of seq to list|
    |4|list.index(obj)|Returns the lowest index in list that obj appears|
    |5|list.insert(index, obj)|Inserts object obj into list at offset index|
    |6|list.pop(obj=list[-1])|Removes and returns last object or obj from list|
    |7|list.remove(obj)|Removes object obj from list|
    |8|list.reverse()|Reverses objects of list in place|
    |9|list.sort([func])|Sorts objects of list, use compare func if given|
 
    [Example Script 21 - m2-script21.py](/Examples/Module-2/m2-script21.py)
#
[Main...](https://github.com/ptoraskar/Python-Learning/blob/master/README.md) | [Back...](/Module-2/2_numbers_strings_functions.md) | [Next...](/Module-2/4_tuple.md)
