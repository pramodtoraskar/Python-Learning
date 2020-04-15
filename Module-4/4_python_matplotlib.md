
![](https://www.python.org/static/img/python-logo.png)

## Matplotlib
 - Matplotlib is an amazing visualization library in Python for 2D plots of arrays
 - It is a multi-platform data visualization library built on NumPy arrays and designed to work with the broader SciPy stack
 - First, let us clear our basics
    - Figure 
        - It is a whole figure which contains one or more than one axes or plots.
    - Axes 
        - A figure contains usually more than one axes (plots) and it may contain two or three in case of three-dimensional structure or objects. 
        - Each Axes has a title, an X –label, and Y –label.
    - Axis
        - It takes care of generating graph limits
    - Artists
        - Mostly they are tied to the axes, and whatever we see on the figure like text objects, line2d objects, collection objects. 

    - Basic plots in Matplotlib
    ```python
        from matplotlib import pyplot as plt 
       
        # x-axis values 
        x = [5, 3, 8, 9, 1] 
        
        # Y-axis values 
        y = [6, 4, 9, 4, 2] 
        
        # Function to plot 
        plt.plot(x,y) 
        
        # Function to show the plot 
        plt.show()
    ```
    - Plotting Multiple Sets of Data
    ```python
        x = np.arange(1,5)
        y = x**5
        plt.plot([10,20,30,40],[100,200,300,400],'go', x,y,'r^')
        plt.title("First Plot")
        plt.xlabel("X axis")
        plt.ylabel("Y axis")
        plt.show()
    ```    
    - Bar plot
    ```python
        # x-axis values 
        x = [5, 2, 9, 4, 7] 
        
        # Y-axis values 
        y = [10, 5, 8, 4, 2] 
        
        # Function to plot the bar 
        plt.bar(x,y) 
        
        # function to show the plot 
        plt.show()
    ```     
    - Histogram
    ```python
        # Y-axis values 
        y = [10, 5, 8, 4, 2] 
        
        # Function to plot histogram 
        plt.hist(y) 
        
        # Function to show the plot 
        plt.show()
    ```
    - Scatter Plot
    ```python
        # x-axis values 
        x = [5, 2, 9, 4, 7] 
        
        # Y-axis values 
        y = [10, 5, 8, 4, 2] 
        
        # Function to plot scatter 
        plt.scatter(x, y) 
        
        # function to show the plot 
        plt.show()
    ```            
    - Pie Charts
    ```python
        fig = plt.figure()
        ax = fig.add_axes([0,0,1,1])
        ax.axis('equal')
        pro_langs = ['c','c++','java', 'python','php']
        stud = [23,14,32,50,41]
        ax.pie(stud,labels=pro_langs,autopct="%1.2f%%")
        plt.show()
    ```
#
[Main...](https://github.com/ptoraskar/Python-Learning/blob/master/README.md) | [Back...](/Module-4/3_python_pandas.md)