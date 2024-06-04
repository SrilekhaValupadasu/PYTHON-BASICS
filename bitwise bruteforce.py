l=int(input("enter number:"))
r=int(input("enter number:"))
for i in range(l,r+1):
    l=l^i
print(l)