print("-"*70)
print("\t\t\tarmstron number ")
print("-"*70)
x=(input("enter the armstrong number :"))
sum=0
for i in x:
    a=int(i)
    b=a**3
    sum+=b

if int(x)==sum:
    print("the given number {} is armstrong number ".format(x))
else:
    print("the given number {} is not armstrong number ".format(x))
print("-"*70)
