def fun():
    print("Welcome to GFG")
fun() # Driver code to call a function

print("================================================")

def evenOdd(x):
    if (x % 2 == 0):
        return "Even"
    else:
        return "Odd"

print(evenOdd(16))
print(evenOdd(7))

print("=======================Default Arguments=========================")

def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)

myFun(10)

print("=======================Keyword Arguments order doesn’t matter =========================")


def student(fname, lname):
    print(fname, lname)

student(fname='Geeks', lname='Practice')
student(lname='Practice', fname='Geeks')

print("=======================positional arguments, values are assigned to parameters based on their order =========================")

def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is ", age)

print("Case-1:")
nameAge("Suraj", 27)

print("\nCase-2:")
nameAge(27, "Suraj")


print("=======================Arbitrary Arguments =========================")
def myFun(*args, **kwargs):
    print("Non-Keyword Arguments (*args):")
    for arg in args:
        print(arg)

    print("\nKeyword Arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key} == {value}")

# Function call with both types of arguments
myFun('Hey', 'Welcome', first='Geeks', mid='for', last='Geeks')



print("======================Function within Functions =========================")

def f1():
    s = 'I love GeeksforGeeks'

    def f2():
        print(s)

    f2()


f1()


print("======================Return Statement in Function =========================")

def square_value(num):
    """This function returns the square
    value of the entered number"""
    return num**2

print(square_value(2))
print(square_value(-4))

print("======================Pass by Reference and Pass by Value=========================")

# Mutable objects: Changes inside the function affect the original object.
# Immutable objects: The original value remains unchanged.


# Function modifies the first element of list
def myFun(x):
    x[0] = 20

lst = [10, 11, 12, 13]
myFun(lst)
print(lst)   # list is modified

# Function tries to modify an integer
def myFun2(x):
    x = 20
    print("Inside function:", x)
a = 10
myFun2(a)
    # integer is not modified
print("Outside function:", a)