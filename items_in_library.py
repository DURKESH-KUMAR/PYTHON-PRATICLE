print("-"*70)
print("\t\t\titems present in the library")
print("-"*70)
x=[]
a=int(input("enter the how much books to be added :"))
for i in range(1,a+1):
    print("enter the name of the book {}:".format(i))
    y=input("enter the name :")
    x.append(y)
print("total books present in the library :",x)
print("-"*70)
    
