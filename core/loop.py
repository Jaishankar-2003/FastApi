n =  4

for i in range (0,n):
    print(i)

li = ["geeks", "for", "geeks"]
for x in li:
    print(x)

tup = ("geeks", "for", "geeks")
for x in tup:
    print(x)

s = "abc"
for x in s:
    print(x)

d = dict({'x': 123, 'y': 354})
for x in d:
    print("%s  %d" % (x, d[x]))

set1 = {10, 30, 20}
for x in set1:
    print(x),


li = ["geeks", "for", "geeks"]
for index in range(len(li)):
    print(li[index])

la = ["geeks", "for", "geeks"]
for index in range(len(la)):
    print(la[index])

tup = ("geeks", "for", "geeks")
for x in tup:
    print(x)


for i in range (4):
    for j in range(4):
        print("*", end=" ")
    print()
# * * * *
# * * * *
# * * * *
# * * * *
print("================================================")
for i in range (0,5):
    for j in range(i):
        print("*", end=" ")
    print()
# *
# * *
# * * *
# * * * *
print("================================================")

for i in range (4,0,-1):
    for j in range(i):
        print("*", end=" ")
    print()

print("================================================")

n = 4
for i in range(1, n + 1):
    print(" " * (n - i), end="")   # spaces
    print("* " * i)                # stars
