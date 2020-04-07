
![](https://www.python.org/static/img/python-logo.png)

# Numbers, Strings Functions


## Numbers

 - Python supports four different numerical types
 
    - int (signed integers)
    - long (long integers )
    - float (floating point real values) - real numbers and are written with a decimal point.
    - complex (complex numbers) - a + bJ
    
 - Number Type Conversion
 
    - int(x) to convert x to a plain integer.
    - long(x) to convert x to a long integer.
    - float(x) to convert x to a floating-point number.
    - complex(x) to convert x to a complex number with real part x and imaginary part zero.
    - complex(x, y) to convert x and y to a complex number with real part x and imaginary part y. 
      x and y are numeric expressions
 
 - Mathematical Functions
 
    - abs(x) The absolute value of x: the (positive) distance between x and zero.
    - cmp(x, y) 
        -1 if x < y 
        0 if x == y 
        1 if x > y
    - max(x1, x2,...) The largest of its arguments: the value closest to positive infinity
    - min(x1, x2,...) The smallest of its arguments: the value closest to negative infinity
    - round(x [,n]) x rounded to n digits from the decimal point.  
 

## Strings

 - Create them simply by enclosing characters in quotes
    ```python
       str_var = "Python Programming"
    ```
 
 - Accessing Values in Strings
    ```python
       str_var = "Python Programming"
       print("str_var[0]: ", str_var[0])
       print("str_var[1:5]: ", str_var[1:15])
    ```
 
 - Updating Strings
    ```python
       str_var = "Python Programming!"
       print("Updated String :- ", str_var[:18] + '2020')
    ```
 
 - String Special Operators
 
    | Operator  | Description    | Syntax                     |
    |-----------|----------------|----------------------------|
    | +         | Concatenation  | a + b                      |
    | *         | Repetition     | a * b                      |
    | []        | Slice          | a[1]                       |
    | [:]       | Range Slice    | a[1:4]                     |
    | in        | Membership     | 'P' in str_var return 1    |
    | not in    | Membership     | 'X' not in str_var return 1|    
 
 - String Formatting
 
    ```python
    print("Red Hat Names Paul Cormier %s and %s" %('President', "Chief Executive Officer"))

    print("Red Hat Names Paul Cormier {} and {}".format('President', "Chief Executive Officer"))

    print( f"Red Hat Names Paul Cormier {'President'} and {'Chief Executive Officer'}") 
    ```
    
 - Built-in String Methods
 
    | Sr.No.| Methods                           |   Description
    |-------|-----------------------------------|--------------------------------------------------------------------------------------------------------------------------|
    | 1	    | capitalize()| Capitalizes first letter of string|
    | 2	    | center(width, fillchar)| Returns a space-padded string with the original string centered to a total of width columns.|
    | 3	    | count(str, beg= 0,end=len(string))| Counts how many times str occurs in string or in a substring of string if starting index beg and ending index end are given.|
    | 4	    | decode(encoding='UTF-8',errors='strict')| Decodes the string using the codec registered for encoding. encoding defaults to the default string encoding.|
    | 5	    | encode(encoding='UTF-8',errors='strict')|Returns encoded string version of string; on error, default is to raise a ValueError unless errors is given with 'ignore' or 'replace'.|
    | 6	    | endswith(suffix, beg=0, end=len(string))|Determines if string or a substring of string (if starting index beg and ending index end are given) ends with suffix; returns true if so and false otherwise.|
    | 7	    | expandtabs(tabsize=8)|Expands tabs in string to multiple spaces; defaults to 8 spaces per tab if tabsize not provided.|
    | 8	    | find(str, beg=0 end=len(string))|Determine if str occurs in string or in a substring of string if starting index beg and ending index end are given returns index if found and -1 otherwise.|
    | 9	    | index(str, beg=0, end=len(string))|Same as find(), but raises an exception if str not found.|
    | 10	| isalnum()|Returns true if string has at least 1 character and all characters are alphanumeric and false otherwise.|
    | 11	| isalpha()|Returns true if string has at least 1 character and all characters are alphabetic and false otherwise.|
    | 12	| isdigit()|Returns true if string contains only digits and false otherwise.|
    | 13	| islower()|Returns true if string has at least 1 cased character and all cased characters are in lowercase and false otherwise.|
    | 14	| isnumeric()|Returns true if a unicode string contains only numeric characters and false otherwise.|
    | 15	| isspace()|Returns true if string contains only whitespace characters and false otherwise.|
    | 16	| istitle()|Returns true if string is properly "titlecased" and false otherwise.|
    | 17	| isupper()|Returns true if string has at least one cased character and all cased characters are in uppercase and false otherwise.|
    | 18	| join(seq)|Merges (concatenates) the string representations of elements in sequence seq into a string, with separator string.|
    | 19	| len(string)|Returns the length of the string|
    | 20    | ljust(width[, fillchar])|Returns a space-padded string with the original string left-justified to a total of width columns.|
    | 21    | lower()|Converts all uppercase letters in string to lowercase.|
    | 22    | lstrip()|Removes all leading whitespace in string.|
    | 23    | maketrans()|Returns a translation table to be used in translate function.|
    | 24    | max(str)|Returns the max alphabetical character from the string str.|
    | 25    | min(str)|Returns the min alphabetical character from the string str.|
    | 26	| replace(old, new [, max])|Replaces all occurrences of old in string with new or at most max occurrences if max given.|
    | 27	| rfind(str, beg=0,end=len(string))|Same as find(), but search backwards in string.|
    | 28	| rindex( str, beg=0, end=len(string))|Same as index(), but search backwards in string.|
    | 29	| rjust(width,[, fillchar])|Returns a space-padded string with the original string right-justified to a total of width columns.|
    | 30    | rstrip()|Removes all trailing whitespace of string.|
    | 31	| split(str="", num=string.count(str))||Splits string according to delimiter str (space if not provided) and returns list of substrings; split into at most num substrings if given.|
    | 32	| splitlines( num=string.count('\n'))|Splits string at all (or num) NEWLINEs and returns a list of each line with NEWLINEs removed.|
    | 33	| startswith(str, beg=0,end=len(string))|Determines if string or a substring of string (if starting index beg and ending index end are given) starts with substring str; returns true if so and false otherwise.|
    | 34	| strip([chars])|Performs both lstrip() and rstrip() on string.|
    | 35	| swapcase()|Inverts case for all letters in string.|
    | 36	| title()|Returns "titlecased" version of string, that is, all words begin with uppercase and the rest are lowercase.|
    | 37	| translate(table, deletechars="")|Translates string according to translation table str(256 chars), removing those in the del string.|
    | 38    | upper()|Converts lowercase letters in string to uppercase.|
    | 39    | zfill (width)|Returns original string leftpadded with zeros to a total of width characters; intended for numbers, zfill() retains any sign given (less one zero).|
    | 40	| isdecimal()|Returns true if a unicode string contains only decimal characters and false otherwise.|     

#
[Main...](https://github.com/ptoraskar/Python-Learning/blob/master/README.md) | [Back...](/Module-2/1_file_functions.md) | [Next...](/Module-2/3_list.md)
