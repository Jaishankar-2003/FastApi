# name = input("enter : ")
# print("onum ela", name  , "vechru")



import keyword
print("The list of keywords are : ")
print(keyword.kwlist)




s = "brand"
age = 25
city = "mdu"
print(s,age,city)




a = "Hello World"
b = 10
c = 11.22
d = ("Geeks", "for", "Geeks" , 23)
e = ["Geeks", "for", "Geeks"]
f = {"Geeks": 1, "for":2, "Geeks":3}


print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)


# | Feature      | List | Tuple | Dict      |
# | ------------ | ---- | ----- | --------- |
# | Brackets     | `[]` | `()`  | `{}`      |
# | Ordered      | ✅    | ✅     | Key-based |
# | Mutable      | ✅    | ❌     | ✅         |
# | Index Access | ✅    | ✅     | ❌         |
# | Key Access   | ❌    | ❌     | ✅         |
# | Duplicates   | ✅    | ✅     | Keys ❌    |



s = "10"
n = int(s)

cnt = 5
f = float(cnt)

age = 25
s2 = str(age)

print(n)
print(f)
print(s2)

# Type Casting a Variable
# Type casting refers to the process of converting the value of one data type into another. Python provides several built-in functions to facilitate casting, including int(), float() and str() among others. Basic casting functions are:
# int(): Converts compatible values to an integer.
# float(): Transforms values into floating-point numbers.
# str(): Converts any data type into a string.



n = 42
f = 3.14
s = "Hello, World!"
li = [1, 2, 3]
d = {'key': 'value'}
bool = True

print(type(n))
print(type(f))
print(type(s))
print(type(li))
print(type(d))
print(type(bool))


age = 19
if age > 18: print("Eligible to Vote.")


age = 10
if age <= 12:
    print("Travel for free.")
else:
    print("Pay for ticket.")


marks = 45
res = "Pass" if marks >= 40 else "Fail"
print(f"Result: {res}")



age = 25
if age <= 12:
    print("Child.")
elif age <= 19:
    print("Teenager.")
elif age <= 35:
    print("Young adult.")
else:
    print("Adult.")

