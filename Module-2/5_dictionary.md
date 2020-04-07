
![](https://www.python.org/static/img/python-logo.png)

## Dictionary
 - An unordered collection of data values, used to store data values like a map
 - key:value pair

     ```python
        dict_obj = {'Training': 'Python Learning', 'Attendees': 25, 'Mode': 'virtual'}
        print("dict_obj['Training']: ", dict_obj['training'])
        print("dict_obj['Mode']: ", dict_obj['mode'])
     ```

 - Updating

    ```python    
        dict_obj = {'Training': 'Python Learning', 'Attendees': 25, 'Mode': 'virtual'}
        
        # Update existing entry
        dict_obj['Attendees'] = 45
     
        # Add new entry
        dict_obj['Location'] = 'Pune'
        
        print("dict_obj['Attendees']: ", dict['Attendees'])
        print("dict_obj['Location']: ", dict['Location'])
    ```
    
 - Delete

    ```python
       dict_obj = {'Training': 'Python Learning', 'Attendees': 25, 'Mode': 'virtual', 'Location': 'Pune'}
       
        # remove entry with key 'Location'
       del dict_obj['Location']
    
       # remove all entries in dict
       dict_obj.clear()
       
       # delete entire dictionary
       del dict_obj

       print("dict['Location']: ", dict['Location'])
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
    
 - Built-in Functions & Methods
 
    |Sr.No.|Function|Description|
    |------|--------|-----------|
    |1|cmp(dict1, dict2)|Compares elements of both dict.|
    |2|len(dict)|Gives the total length of the dictionary. This would be equal to the number of items in the dictionary.|
    |3|str(dict)|Produces a printable string representation of a dictionary|
    |4|type(variable)|Returns the type of the passed variable. If passed variable is dictionary, then it would return a dictionary type.|
    
    - Python includes following dictionary methods
    
    |Sr.No.|Methods|Description|
    |------|--------|-----------|
    |1|dict.clear()|Removes all elements of dictionary dict|
    |2|dict.copy()|Returns a shallow copy of dictionary dict|
    |3|dict.fromkeys()|Create a new dictionary with keys from seq and values set to value.|
    |4|dict.get(key, default=None)|For key key, returns value or default if key not in dictionary|
    |5|dict.has_key(key)|Returns true if key in dictionary dict, false otherwise|
    |6|dict.items()|Returns a list of dict's (key, value) tuple pairs|
    |7|dict.keys()|Returns list of dictionary dict's keys|
    |8|dict.setdefault(key, default=None)|Similar to get(), but will set dict[key]=default if key is not already in dict|
    |9|dict.update(dict2)|Adds dictionary dict2's key-values pairs to dict|
    |10|dict.values()|Returns list of dictionary dict's values| 
 [Example Script 23 - m2-script23.py](/Examples/Module-2/m2-script23.py)
#
[Main...](https://github.com/ptoraskar/Python-Learning/blob/master/README.md) | [Back...](/Module-2/4_tuple.md) | [Next...](/Module-2/6_set.md)
