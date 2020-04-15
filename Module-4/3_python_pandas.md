
![](https://www.python.org/static/img/python-logo.png)

## Pandas
 - Pandas DataFrame is two-dimensional size-mutable, potentially heterogeneous tabular data structure with labeled axes (rows and columns). 
 - A Data frame is a two-dimensional data structure, i.e., data is aligned in a tabular fashion in rows and columns. 
 - Pandas DataFrame consists of three principal components, the data, rows, and columns.
 
 - Create Series and Data Frames in Pandas
    - A Pandas DataFrame will be created by loading the datasets from existing storage, storage can be SQL Database, CSV file, and Excel file. 
    - Pandas DataFrame can be created from the lists, dictionary, and from a list of dictionary etc.
        - Creating an empty dataframe
            - A basic DataFrame, which can be created is an Empty Dataframe. 
            - An Empty Dataframe is created just by calling a dataframe constructor.
        ```python
            import pandas as pd 
            
            # Calling DataFrame constructor 
            df = pd.DataFrame() 
            print(df)
        ```
        - From List    
        ```python
            # To create data frame, import pandas as pd
            import pandas as pd
            
            # list of strings
            list_obj = ["Nikita Asrani",
                        "Pravin Galande",
                        "Rayan Mariyan",
                        "Sanjeevani Koli",
                        "Sagar Yadav",
                        "Vikram Kumar",
                        "Inder Punj",
                        "Manoranjan Singh",
                        "Sagar Wagh"]
            # Calling DataFrame constructor on list
            df_obj = pd.DataFrame(list_obj)
            print(df_obj)
        ```
        - From dict of ndarray/lists
        ```python
            # Program demonstrate creating DataFrame from dict narray / lists
            import pandas as pd
             
            # Initialize data of lists.
            data = {'Name':['Pravin', 'Rayan', 'Sagar', 'Inder'], 'Age':[23, 21, 34, 27]}
             
            # Create DataFrame
            df = pd.DataFrame(data)
             
            # Print the output.
            print(df)
        ```
 - Basic operations
    - Column Selection
        - To select a column in Pandas DataFrame, access the columns by calling them by their columns name.
        ```python
            import pandas as pd
            # Define a dictionary containing employee data
            data = {'Name':['Pravin', 'Rayan', 'Sagar', 'Inder'],
                    'Age':[27, 24, 22, 32],
                    'Address':['Delhi', 'Kanpur', 'Allahabad', 'Pune'],
                    'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
            
            # Convert the dictionary into DataFrame 
            df = pd.DataFrame(data)
             
            # select two columns
            print(df[['Name', 'Qualification']])
        ```    
    - Row Selection
        - DataFrame.loc[] method is used to retrieve rows from Pandas DataFrame. 
        - Rows can also be selected by passing integer location to an iloc[] function.
        ```python
            import pandas as pd
            data = pd.read_csv("Examples/Module-4/nba.csv", index_col ="Name")
            # retrieving row by loc method
            first = data.loc["Avery Bradley"]
            second = data.loc["R.J. Hunter"]
            print(first,"\n\n\n",second)
        ```   
 - Importing and exporting data
    - Export the DataFrame to CSV/Excel File
        ```python
        # Import pandas library first

        import pandas as pd
        
        students_df = {'Name':['Pravin', 'Rayan', 'Sagar', 'Inder'],
                     'Age':[27, 24, 22, 32],
                     'Address':['Delhi', 'Kanpur', 'Allahabad', 'Pune'],
                      'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
       
        # Create DataFrame
        df = pd.DataFrame(students_df, columns= ['Name', 'Age', 'Address', 'Qualification'])

        # Export DataFrame to CSV File
        export_csv = df.to_csv (r'Examples/Module-4/test_dataframe.csv', index = None, header=True)
  
        df.to_excel(r'Examples/Module-4/test_dataframe.xlsx')
        
        print(df)
        ```
    - Import/Load dataframe in from CSV/Excel File
        ```python
        import pandas as pd
        df = pd.read_csv('Examples/Module-4/test_dataframe.csv')
        df.head()
  
        df = pd.read_excel(r'Examples/Module-4/test_dataframe.xlsx')
        print(df)
        ```
 - Indexing and Selecting
    - Indexing in pandas means simply selecting particular rows and columns of data from a DataFrame. 
    - Indexing could mean selecting all the rows and some of the columns, some of the rows and all of the columns, or some of each of the rows and columns. 
    - Indexing can also be known as Subset Selection.
        - Indexing a Dataframe using indexing operator []
            - The .loc and .iloc indexers also use the indexing operator to make selections. 
            - In this indexing operator to refer to df[]
            ```python
            # importing pandas package
            import pandas as pd
             
            # making data frame from csv file
            data = pd.read_csv("Examples/Module-4/nba.csv", index_col ="Name")
             
            # retrieving columns by indexing operator
            first = data["Age"]
            
            print(first)
            ```
        - Indexing a DataFrame using .loc[ ] 
            ```python
            # importing pandas package
            import pandas as pd
             
            # making data frame from csv file
            data = pd.read_csv("Examples/Module-4/nba.csv", index_col ="Name")
             
            # retrieving row by loc method
            first = data.loc["Avery Bradley"]
            second = data.loc["R.J. Hunter"]
            
            print(first, "\n\n\n", second)
            ```
        - Indexing a DataFrame using .iloc[ ]
            ```python
            import pandas as pd
             
            # making data frame from csv file
            data = pd.read_csv("Examples/Module-4/nba.csv", index_col ="Name")
             
            # retrieving rows by iloc method 
            row2 = data.iloc[3] 
             
            print(row2)
            ```
 - Iterating over rows and columns
    - Pandas DataFrame consists of rows and columns so, in order to iterate over dataframe, 
    - We have to iterate a dataframe like a dictionary.
    - To iterate over rows, we can use three function iteritems(), iterrows(), itertuples().
    - Iterating over rows
        ```python
            import pandas as pd
              
            # Dictionary of lists
            dict_obj = {'name':['Pravin', 'Rayan', 'Sagar', 'Inder'],
                    'degree': ["MBA", "BCA", "M.Tech", "MBA"],
                    'score':[90, 40, 80, 98]}
            # Creating a dataframe from a dictionary 
            df = pd.DataFrame(dict)
             
            # iterating over rows using iterrows() function 
            for i, j in df.iterrows():
                print(i, j)
                print()
        ```
    - Iterating over Columns
        ```python
            import pandas as pd
               
            # dictionary of lists
            dict = {'name':['Pravin', 'Rayan', 'Sagar', 'Inder'],
                    'degree': ["MBA", "BCA", "M.Tech", "MBA"],
                    'score':[90, 40, 80, 98]}
            # creating a dataframe from a dictionary 
            df = pd.DataFrame(dict)
            print(df)
            
            # creating a list of dataframe columns
            columns = list(df)
             
            for i in columns:
                # printing the third element of the column
                print (df[i][2])
        ```

 - Pandas Working With Text Data
    - Series and Indexes are equipped with a set of string processing methods that make it easy to operate on each 
      element of the array.
    - Perhaps most importantly, these methods exclude missing/NA values automatically.

    - Update Casing [Lowercasing and Uppercasing a Data]
        ```python
            import pandas as pd 
               
            # Define a dictionary containing employee data 
            data = {'Name':['Pravin', 'Rayan', 'Sagar', 'Inder'], 
                    'Age':[27, 24, 22, 32], 
                    'Address':['Delhi', 'Kanpur', 'Allahabad', 'Pune'], 
                    'Qualification':['Msc', 'MA', 'MCA', 'Phd']} 
            
            # Convert the dictionary into DataFrame  
            df = pd.DataFrame(data) 
               
            # Converting and overwriting values in column 
            df["Name"]= df["Name"].str.lower()
            
            print(df)
        ```        
    - Splitting and Replacing a Data
        - We use str.split() this function returns a list of strings after breaking the given string by the specified 
          separator but it can only be applied to an individual string
        - Pandas str.split() method can be applied to a whole series. .str has to be prefixed every time before 
          calling this method to differentiate it from the Python’s default function otherwise, it will throw an error.
        ```python
            import pandas as pd 
                 
            # Define a dictionary containing employee data 
            data = {'Name':['Pravin', 'Rayan', 'Sagar', 'Inder'], 
                    'Age':[27, 24, 22, 32], 
                    'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Pune'], 
                    'Qualification':['Msc', 'MA', 'MCA', 'Phd']} 
             
            # Convert the dictionary into DataFrame  
            df = pd.DataFrame(data) 
                
            # dropping null value columns to avoid errors 
            df.dropna(inplace = True) 
                
            # new data frame with split value columns 
            df["Address"]= df["Address"].str.split("a", n = 1, expand = True) 
               
            # df display 
            print(df)
        ```          
        - To replace a data, we use str.replace() this function works like Python .replace() method only, but it works 
          on Series too   
        ```python
            import pandas as pd
             
            # reading csv file from url
            data = pd.read_csv("Examples/Module-4/nba.csv")
             
            # overwriting column with replaced value of age
            data["Age"]= data["Age"].replace(25.0, "Twenty five")
             
            # creating a filter for age column 
            # where age = "Twenty five"
            filtered_date = data["Age"]=="Twenty five"
             
            # printing only filtered columns
            data.where(filtered_date).dropna()
        ```

 - Pandas Merging, Joining, and Concatenating

    - Concatenating DataFrame
        - We use .concat() function this function concat a dataframe and returns a new dataframe
        ```python
            import pandas as pd 
                 
            # Define a dictionary containing employee data  
            emp_obj_1 = {'Name':['Pravin', 'Rayan', 'Sagar', 'Inder'],
                          'Age':[27, 24, 22, 32], 
                          'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Pune'], 
                          'Qualification':['Msc', 'MA', 'MCA', 'Phd']} 

            # Define a dictionary containing employee data 
            emp_obj_2 = {'Name':['Gaurav', 'Dushyen', 'Sanjeevani', 'Manoranjan'], 
                          'Age':[17, 14, 12, 52], 
                          'Address':['Delhi', 'Kota', 'Sangareddy', 'Kannuaj'], 
                          'Qualification':['Btech', 'B.A', 'Bcom', 'B.hons']}
 
             # Convert the dictionary into DataFrame  
            df_obj_1 = pd.DataFrame(emp_obj_1,index=[0, 1, 2, 3])
             
            # Convert the dictionary into DataFrame  
            df_obj_2 = pd.DataFrame(emp_obj_2, index=[4, 5, 6, 7])

            print(df_obj_1, "\n\n", df_obj_2)

            # Using a .concat() method
            frames = [df_obj_1, df_obj_2]
            res_df = pd.concat(frames)
            print(res_df)           
        ```
        - Now we set axes join = inner for intersection of dataframe
        ```python
        
            # Define a dictionary containing employee data 
            emp_obj_1 = {'Name':['Pravin', 'Rayan', 'Sagar', 'Inder'], 
                    'Age':[27, 24, 22, 32], 
                    'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
                    'Qualification':['Msc', 'MA', 'MCA', 'Phd'],
                    'Mobile No': [97, 91, 58, 76]} 
               
            # Define a dictionary containing employee data 
            emp_obj_2 = {'Name':['Gaurav', 'Dushyen', 'Sanjeevani', 'Manoranjan'], 
                    'Age':[22, 32, 12, 52], 
                    'Address':['Allahabad', 'Kannuaj', 'Allahabad', 'Kannuaj'], 
                    'Qualification':['MCA', 'Phd', 'Bcom', 'B.hons'],
                    'Salary':[1000, 2000, 3000, 4000]} 
             
            # Convert the dictionary into DataFrame  
            df_obj_1 = pd.DataFrame(emp_obj_1,index=[0, 1, 2, 3])
             
            # Convert the dictionary into DataFrame  
            df_obj_2 = pd.DataFrame(emp_obj_2, index=[2, 3, 6, 7]) 
            
            print(df_obj_1, "\n\n", df_obj_2)
            
            # Applying concat with axes join = 'inner'
            res_df_2 = pd.concat([df_obj_1, df_obj_2], axis=1, join='inner')
            res_df_2
        ```
        - Now we set axes join = outer for union of dataframe.
        ```python
            # Using a .concat for union of dataframe
            res_df_2 = pd.concat([df_obj_1, df_obj_2], axis=1, sort=False)
            res_df_2
        ```

        - Concatenating DataFrame using .append()
            - To concat a dataframe, we use .append() function this function concatenate along axis=0, namely the index
        ```python
        
            # Define a dictionary containing employee data 
            emp_obj_1 = {'Name':['Pravin', 'Rayan', 'Sagar', 'Inder'], 
                    'Age':[27, 24, 22, 32], 
                    'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
                    'Qualification':['Msc', 'MA', 'MCA', 'Phd'],
                    'Mobile No': [97, 91, 58, 76]} 
               
            # Define a dictionary containing employee data 
            emp_obj_2 = {'Name':['Gaurav', 'Dushyen', 'Sanjeevani', 'Manoranjan'], 
                    'Age':[22, 32, 12, 52], 
                    'Address':['Allahabad', 'Kannuaj', 'Allahabad', 'Kannuaj'], 
                    'Qualification':['MCA', 'Phd', 'Bcom', 'B.hons'],
                    'Salary':[1000, 2000, 3000, 4000]}  
             
            # Convert the dictionary into DataFrame
            df_obj_1 = pd.DataFrame(emp_obj_1,index=[0, 1, 2, 3])
             
            # Convert the dictionary into DataFrame  
            df_obj_2 = pd.DataFrame(emp_obj_2, index=[4, 5, 6, 7])
             
            print(df_obj_1, "\n\n", df_obj_2) 
            
            # Using append function
             
            res_df = df_obj_1.append(df_obj_2)
            res_df
        ```                        
        - Concatenating DataFrame with group keys
        ```python
            # Convert the dictionary into DataFrame  
            df_obj_1 = pd.DataFrame(emp_obj_1,index=[0, 1, 2, 3])
             
            # Convert the dictionary into DataFrame  
            df_obj_2 = pd.DataFrame(emp_obj_2, index=[4, 5, 6, 7])
             
            print(df_obj_1, "\n\n", df_obj_2)  
            
            # using keys 
            frames = [df_obj_1, df_obj_2]
             
            res_df = pd.concat(frames, keys=['x', 'y'])
            res_df
        ```           
    - Merging DataFrame
        - Pandas have options for high-performance in-memory merging and joining
        - It’s a good practice to use keys which have unique values throughout the column to avoid unintended duplication of row values
        - Pandas provide a single function, merge(), as the entry point for all standard database join operations between DataFrame objects
        - Four basic ways to handle the join 
            > inner, left, right, and outer
        
        - Merging a dataframe with one unique key combination
        ```python
            # Define a dictionary containing employee data 
            emp_obj_1 = {'key': ['Pravin', 'Rayan', 'Sagar', 'Inder'],
                     'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
                     'Age':[27, 24, 22, 32],} 
               
            # Define a dictionary containing employee data 
            emp_obj_2 = {'key': ['K0', 'K1', 'K2', 'K3'],
                     'Address':['Allahabad', 'Kannuaj', 'Allahabad', 'Kannuaj'], 
                     'Qualification':['Btech', 'B.A', 'Bcom', 'B.hons']} 
             
            # Convert the dictionary into DataFrame  
            df_obj_1 = pd.DataFrame(emp_obj_1)
             
            # Convert the dictionary into DataFrame  
            df_obj_2 = pd.DataFrame(emp_obj_1) 
              
             
            print(df_obj_1, "\n\n", df_obj_2) 
            
            # using .merge() function
            res_df = pd.merge(df_obj_1, df_obj_2, on='key')
             
            res_df
        ```
        - Merging dataframe using multiple join keys
        ```python
            # Define a dictionary containing employee data 
            emp_obj_1 = {'key': ['K0', 'K1', 'K2', 'K3'],
                     'key1': ['K0', 'K1', 'K0', 'K1'],
                     'Name':['Pravin', 'Rayan', 'Sagar', 'Inder'], 
                    'Age':[27, 24, 22, 32],} 
               
            # Define a dictionary containing employee data 
            emp_obj_2 = {'key': ['K0', 'K1', 'K2', 'K3'],
                     'key1': ['K0', 'K0', 'K0', 'K0'],
                     'Address':['Allahabad', 'Kannuaj', 'Allahabad', 'Kannuaj'], 
                    'Qualification':['Btech', 'B.A', 'Bcom', 'B.hons']} 
             
            # Convert the dictionary into DataFrame  
            df_obj_1 = pd.DataFrame(emp_obj_1)
             
            # Convert the dictionary into DataFrame  
            df_obj_2 = pd.DataFrame(emp_obj_2) 
              
             
            print(df_obj_1, "\n\n", df_obj_2) 
            
            # merging dataframe using multiple keys
            res_df = pd.merge(df_obj_1, df_obj_1, on=['key', 'key1'])
             
            res_df
        ```
        - Merging dataframe using how in an argument
            - We use **how** argument to merge specifies how to determine which keys are to be included in the resulting table

            |MERGE METHOD|JOIN NAME|DESCRIPTION|
            |---|---|---|
            |left|LEFT OUTER JOIN|Use keys from left frame only|
            |right|RIGHT OUTER JOIN|Use keys from right frame only|
            |outer|FULL OUTER JOIN|Use union of keys from both frames|
            |inner|INNER JOIN|Use intersection of keys from both frames|                                

        - Now we set how = 'left' in order to use keys from left frame only.
        ```python
            # using keys from left frame
            res_df = pd.merge(df_obj_1, df_obj_1,  how='left', on=['key', 'key1'])
            res_df
        ```
        - Now we set how = 'right' in order to use keys from right frame only.
        ```python
            # using keys from left frame
            res_df = pd.merge(df_obj_1, df_obj_1,  how='right', on=['key', 'key1'])
            res_df
        ```
        - Now we set how = 'outer' in order to get union of keys from dataframes.
        ```python
            # using keys from left frame
            res_df = pd.merge(df_obj_1, df_obj_1,  how='outer', on=['key', 'key1'])
            res_df
        ```
        - Now we set how = 'inner' in order to get intersection of keys from dataframes.
        ```python
            # using keys from left frame
            res_df = pd.merge(df_obj_1, df_obj_1,  how='inner', on=['key', 'key1'])
            res_df
        ```

    - Joining DataFrame
        - To join dataframe, we use **.join()** function this function is used for combining the columns of two potentially 
        differently-indexed DataFrames into a single result DataFrame
        
        ```python
            # Define a dictionary containing employee data 
            emp_obj_1 = {'Name':['Pravin', 'Rayan', 'Sagar', 'Inder'], 
                         'Age':[27, 24, 22, 32]} 
                
            # Define a dictionary containing employee data 
            emp_obj_2 = {'Address':['Allahabad', 'Kannuaj', 'Allahabad', 'Kannuaj'], 
                         'Qualification':['MCA', 'Phd', 'Bcom', 'B.hons']} 
              
            # Convert the dictionary into DataFrame  
            df_obj_1 = pd.DataFrame(emp_obj_1,index=['K0', 'K1', 'K2', 'K3'])
              
            # Convert the dictionary into DataFrame  
            df_obj_2 = pd.DataFrame(emp_obj_2, index=['K0', 'K2', 'K3', 'K4'])
            
            
            print(df_obj_1, "\n\n", df_obj_2)  
            
            # joining dataframe
            res_df_1 = df_obj_1.join(df_obj_2)
             
            res_df_1
        ```
        - Now we use how = 'outer' in order to get union
        ```python
            # getting union
            res_df_1 = df_obj_1.join(df_obj_2, how='outer')
             
            res_df_1
        ```
        - Joining dataframe using **on** in an argument
            - To join dataframes we use on in an argument. join() takes an optional on argument which may be a column 
            or multiple column names, which specifies that the passed DataFrame is to be aligned on that column in 
            the DataFrame
        
        ```python
            # Define a dictionary containing employee data 
            emp_obj_1 = {'Name':['Pravin', 'Rayan', 'Sagar', 'Inder'], 
                    'Age':[27, 24, 22, 32],
                    'Key':['K0', 'K1', 'K2', 'K3']} 
                
            # Define a dictionary containing employee data 
            emp_obj_2 = {'Address':['Allahabad', 'Kannuaj', 'Allahabad', 'Kannuaj'], 
                    'Qualification':['MCA', 'Phd', 'Bcom', 'B.hons']} 
              
            # Convert the dictionary into DataFrame  
            df_obj_1 = pd.DataFrame(emp_obj_1)
              
            # Convert the dictionary into DataFrame  
            df_obj_2 = pd.DataFrame(emp_obj_2, index=['K0', 'K2', 'K3', 'K4'])
             
            print(df_obj_1, "\n\n", df_obj_2)
            
            # using on argument in join
            res_df = df_obj_1.join(df_obj_2, on='Key')
             
            res_df
        ```
    - **Join** and **Merge**
        - We can use **join** and **merge** to combine 2 dataframes.
        - The **join** method works best when we are joining dataframes on their indexes (though you can specify another column to join on for the left dataframe).
        - The **merge** method is more versatile and allows us to specify columns besides the index to join on for both dataframes. If the index gets reset to a counter post merge, we can use set_index to change it back.
#
[Main...](https://github.com/ptoraskar/Python-Learning/blob/master/README.md) | [Back...](/Module-4/2_python_numpy.md) | [Next...](/Module-4/4_python_matplotlib.md)