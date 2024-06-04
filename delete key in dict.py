import operator
d = {}
n = int(input("no.of elements:"))
for i in range(n):
    key=int(input("enter key of dict:"))
    value=int(input("enter its value:"))
    d[key]=value
key=int(input("enter number to pop:"))
if key in d:
    del d[key]
print(d)