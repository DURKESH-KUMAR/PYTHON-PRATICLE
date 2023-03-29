print("-"*70)
print("\t\t\tstar pattern")
print("-"*70)
x=int(input("enter the range for the star pattern :"))
for i in range(x):
    for j in range(i,x):
        print(" ",end=" ")
    for k in range(0,i+1):
        print("*",end=" ")
    for j in range(0,i):
        print("*",end=" ")
    print(end="\n")
    
