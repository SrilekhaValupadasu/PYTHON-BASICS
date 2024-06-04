d = {}
d1={}
n = int(input("no.of elements:"))
for i in range(n):
    key=input("enter key of dict:")
    value=input("enter its value:")
    d1[key]=value
for i in range(n):
    key=input("enter key for dict:")
    value=input("enter its value:")
    d1[key]=value
d2=d.copy()
d2.update(d1)
print(d2)
