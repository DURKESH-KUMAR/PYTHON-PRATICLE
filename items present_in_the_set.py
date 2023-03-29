print("-"*70)
print("\t\t\titems present in the library")
print("-"*70)
x=set()
y=int(input("enter how much book to be stored :"))

for i in range(1,y+1):
    print("enter the book number: %d"%(i))
    a=input("enter the name :")
    x.add(a)
print("items present in the library :",x)
