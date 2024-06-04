import operator
d = {}  
n = int(input("no.of elements:"))
for i in range(n):
    key=input("enter key of dict:")
    value=input("enter its value:")
    d[key]=value
key=input("enter to update key:")
value=input("enter to update value:")
d.update({key:value})
print(d)