def fun(n):
    if (n<=0):
        return;
    else:
        print(n,end=" ");
        fun(n-1);
n =int(input("enter:"))
fun(n);