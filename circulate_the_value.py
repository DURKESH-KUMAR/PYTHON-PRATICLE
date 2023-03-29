print("-"*70)
print("\t\t\tcirculate the value")
print("-"*70)
x=int(input("enter the start value :"))
y=int(input("enter the end   value :"))
l=list(range(x,y+1))
print("the given list :",l)
for i in range(1,y-x+2):
    a=l[i:]+l[:i]
    print(a)
print("-"*70)
