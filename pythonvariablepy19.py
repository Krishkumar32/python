'''
Variables:
Variables are containers for storing data values.

Creating Variables:
Python has no command for declaring a variable.
A variable is created the moment you first assign a value to it.
'''
# example:
x=5
y=john
print(x)
print(y)
#data type variable:
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#Case-Sensitive
#Variable names are case-sensitive.
#example:
a = 4
A = "Sally"
#A will not overwrite a
'''
Rules for Python variables:
A Python variable name must start with a letter or the underscore character.
A Python variable name cannot start with a number.
A Python variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ ).
Variable in Python names are case-sensitive (name, Name, and NAME are three different variables).
The reserved words(keywords) in Python cannot be used to name the variable in Python.
'''
'''
Variable Types in Python
Data types are the classification or categorization of data items. It represents the kind of value that tells what operations can be performed on a particular data. Since everything is an object in Python programming, data types are actually classes and variables are instances (object) of these classes.

Built-in Python Data types are:
Numeric
Text Type
Sequence Type (Python list, Python tuple, Python range)
Boolean
Set
Dictionary
'''
# numberic
var = 123
print("Numeric data : ", var)

# Sequence Type
String1 = 'Welcome to the Geeks World'
print("String with the use of Single Quotes: ")
print(String1)

# Boolean
print(type(True))
print(type(False))

# Creating a Set with
# the use of a String
set1 = set("GeeksForGeeks")
print("\nSet with the use of String: ")
print(set1)

# Creating a Dictionary
# with Integer Keys
Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print("\nDictionary with the use of Integer Keys: ")
print(Dict)
