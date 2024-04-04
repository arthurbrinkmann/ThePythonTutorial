
#Here's a simple example demonstrating the use of *args in Python:
#
#python
#Copy code
# Define a function that accepts a variable number of arguments
def greet(*args):
    # args is a tuple containing all the positional arguments passed to the function
    for name in args:
        print("Hello,", name)

#greet("Alice", "Bob", "Charlie")  
#greet("David", "Eve")        
#greet("Frank")
greet()