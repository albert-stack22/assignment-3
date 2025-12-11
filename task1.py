def fac(n):
    if (n == 1) :
       return 1
    else:
        return n*fac(n-1)
a=int (input("enter a number :"))
b=fac(a)
print(f"the factorial of {a} is {b}")
