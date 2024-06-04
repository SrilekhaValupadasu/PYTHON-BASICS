import operator
d = {}  
n = int(input("no.of elements:"))
for i in range(n):
    key=input("enter key of dict:")
    value=input("enter its value:")
    d[key]=value
key=input("enter key to find:")
if key in d:
    print("yes")
else:
    print("no")