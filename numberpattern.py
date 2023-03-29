print("-"*70)
print("\t\t\tnumber pattern")
print("-"*70)
x=int(input("enter the range :"))
for i in range(1,x+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print(end="\n")
