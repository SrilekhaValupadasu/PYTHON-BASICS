def fun(n):
    if n>0:
        fun(n-1)
        print(n)
num=int(input("enter:"))
fun(num)


# calling recurion function at first and executed

#head recursion