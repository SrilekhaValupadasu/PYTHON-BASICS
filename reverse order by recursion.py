def fun(n):
    if n>0:
        print(n)
        fun(n-1)
num=int(input("enter:"))
fun(num)

# tail recursion::::something get EXCUTED
#after ecution recurion will be called