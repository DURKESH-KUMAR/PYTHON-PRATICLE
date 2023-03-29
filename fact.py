
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
x=int(input("enter the factorial of the number :"))
print("the factorial is {}".format(fact(x)))

