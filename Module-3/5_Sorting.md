 
![](https://www.python.org/static/img/python-logo.png)
 
## Sorting
####*Sequences, Dictionaries, Limitations of Sorting*

- Sorting Basics¶
   - A simple ascending sort is very easy
    ```python
      print(sorted([5, 2, 3, 1, 4]))
    ``` 
    **Note**: You can also use the list.sort() method
    
   - To sort the list in descending order.
   ```python
      list_num = [5, 2, 3, 1, 4]
      list_num.sort(reverse=True)
    ```
   
   - sorted()
    - The sorted() function accepts any iterable
    ```python
      print(sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'}))
    ```

    - Key Functions¶
        - Both list.sort() and sorted() have a key parameter.
        - To specify a function to be called on each list element prior to making comparisons.
    
    ```python

      student_tuples = [('abc', 'A', 15), ('xyz', 'B', 12), ('pqr', 'B', 10),]

      print(sorted(student_tuples, key=lambda student: student[2]))
    
    ```
#
[Main...](https://github.com/ptoraskar/Python-Learning/blob/master/README.md) | [Back...](Module-3/4_Lambda.md) | [Next...](/Module-3/6_Errors_and_Exceptions.md)