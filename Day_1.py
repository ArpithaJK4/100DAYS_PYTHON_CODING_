print("Hello, World!")

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
print("Hello, World!")

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

#printing variables
x = 5
y = "John"
print(x)
print(y)

#changing the variable type
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#typecasting of the variables
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#checkking the dtatyor of the variables
x = 5
y = "John"
print(type(x))
print(type(y))

# we can declare using single and duble quote
x = "John"
# is the same as
x = 'John'

#pyton is case sensitive
a = 4
A = "Sally"
#A will not overwrite a

#valid variable name

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#illegle variable name
2myvar = "John"
my-var = "John"
my var = "John"
#camel case
myVariableName = "John"
#pascle case
MyVariableName = "John"
#snake case
my_variable_name = "John"
#many values to multiple variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
one value to multiple variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

#Global variable
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()
x = "awesome"

#If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.
def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

#using globle keyword
print("Python is " + x)
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
