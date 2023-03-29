print("-"*70)
print("\t\t\tfibbonnaci series")
print("-"*70)
x=int(input("enter the range of the series :"))
a=0
b=1

for i in range(0,x):
    c=a+b
    print(c,end=" ")
    a=b
    b=c
print(end="\n")
print("-"*70)

