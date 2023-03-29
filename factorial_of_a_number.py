print("-"*70)
print("\t\t\tfactorial of an number :")
print("-"*70)
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
x=int(input("enter the number to factorial :"))
print("hence the factorial of the number {} is {}".format(x,fact(x)))
print("-"*70)
