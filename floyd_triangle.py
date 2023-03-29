print("-"*70)
print("\t\t\tfloyd\'s triangle")
print("-"*70)
n=1
x=int(input("enter the range :"))
for i in range(1,x+1):
    for j in range(0,i):
        print(n,end=" ")
        n+=1
    print()
