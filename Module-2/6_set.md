
![](https://www.python.org/static/img/python-logo.png)

## Sets

 - An unordered collection data type that is iterable, mutable and has no duplicate elements
 - Represents the mathematical notion of a set
 - Advantage of using a set, as opposed to a list, is that it has a highly optimized method for checking whether a 
   specific element is contained in the set
 - As sets are unordered, we cannot access items using indexes like we do in lists. 

     ```python
        # program to demonstrate sets 
        
        # Same as {'E1', 'E2', 'E3'} 
        set_obj = set(['E1', 'E2', 'E3']) 
        print(set_obj) 
        
        # Adding element to the set 
        set_obj.add("E4") 
        print(set_obj) 
     ```

 - Adding

    ```python    
        # Program to demonstrate adding elements in a set 
        
        # Creating a Set 
        attendees = {"Amit", "Nikita", "Sanjeevani", "Vikram"} 
        print("Attendees:", end = " ")
        print(attendees) 

        # This will add Daxit in the set
        attendees.add("Sagar") 

        # Adding elements to the set using iterator 
        for i in range(1, 6):
            attendees.add(i) 

        print("\nSet after adding element:", end = " ") 
        print(attendees) 

    ```
    
 - Union

    - Two sets can be merged using union() or **|** operator

    ```python
       # Program to demonstrate union of two sets 

       attendees = {"Amit", "Nikita", "Sanjeevani", "Vikram"} 
       assignment_complete = {"Dushyen", "Reetika"} 
       assignment_not_complete = {"Pramod", "Mahesh"} 

       # Union using union() function 
       attendees_assignment = attendees.union(assignment_complete) 

       print("Union using union() function") 
       print(attendees_assignment) 

       # Union using "|" operator 
       participants = assignment_complete|assignment_not_complete 

       print("\nUnion using '|' operator") 
       print(participants) 

   ```
 - Intersection

    - This can be done through intersection() or & operator. Common Elements are selected

    ```python
        # Program to demonstrate intersection of two sets 
        
       attendees = {"Amit", "Nikita", "Sanjeevani", "Vikram"} 
       assignment_complete = {"Dushyen", "Nikita"} 
       assignment_not_complete = {"Pramod", "Amit"} 
        
        # Intersection using intersection() function 
        attendees_inter = attendees.intersection(assignment_complete) 
        
        print("Intersection using intersection() function") 
        print(attendees_inter) 
        
        # Intersection using 
        # "&" operator 
        attendees_inter = attendees & assignment_not_complete 
        
        print("\nIntersection using '&' operator") 
        print(attendees_inter) 

    ```
 
 - Difference

    - To find difference in between sets. Similar to find difference in linked list.

    ```python
        # Program demonstrate difference of two sets 
        
        attendees = {"Amit", "Nikita", "Sanjeevani", "Vikram"} 
        assignment_complete = {"Dushyen", "Nikita"} 
        assignment_not_complete = {"Pramod", "Amit"} 

        # Difference of two sets using difference() function 
        attendees_diff = attendees.difference(assignment_complete) 
        
        print(" Difference of two sets using difference() function") 
        print(attendees_diff) 
        
        # Difference of two sets 
        # using '-' operator 
        attendees_diff = attendees - assignment_complete 
        
        print("\nDifference of two sets using '-' operator") 
        print(attendees_diff)
    ```

 - Clearing sets

    - Clear() method empties the whole set.
    
    ```python
        # Program to demonstrate clearing of set 
        set_obj = {'E1', 'E2', 'E3'} 
        
        print("Initial set") 
        print(set_obj) 
        
        # This method will remove 
        # all the elements of the set 
        set_obj.clear() 
        
        print("\nSet after using clear() function") 
        print(set_obj) 

    ```
    
 - Properties
    - More than one entry per key not allowed
    
        ```python        
          dict_obj = {'Training': 'Python Learning', 'Attendees': 25, 'Training': 'Basic Python Learning'}
          print("dict_obj['Training']: ", dict_obj['Training'])
        ```

    - Keys must be immutable

        ```python
          dict_obj = {['Training']: 'Python Learning', 'Attendees': 25, 'Mode': 'virtual'}
          print("dict_obj['Training']: ", dict_obj['Name'])
        ```
    
 - Operators
 
    |sr.no|operators|notes|
    |-----|---------|-----|
    |1|key in s|containment check|
    |2|key not in s|non-containment check|
    |3|set_1 == set_2|set_1 is equivalent to set_2|
    |4|set_1 != set_2|set_1 is not equivalent to set_2|
    |5|set_1 <= set_2|set_1 is subset of set_2|
    |6|set_1 < set_2|set_1 is proper subset of set_2|
    |7|set_1 >= set_2|set_1 is superset of set_2|
    |8|set_1 > set_2|set_1 is proper superset of set_2|
    |9|set_1\|set_2| the union of set_1 and set_2|
    |10|set_1 & set_2|the intersection of set_1 and set_2|
    |11|set_1 – set_2|the set of elements in set_1 but not set_2|
    |12|set_1 ˆ set_2|the set of elements in precisely one of set_1 or set_2|

 [Example Script 24 - m2-script24.py](/Examples/Module-2/m2-script24.py)
#
[Main...](https://github.com/ptoraskar/Python-Learning/blob/master/README.md) | [Back...](/Module-2/4_tuple.md) | [Next...](/Module-2/6_set.md)
