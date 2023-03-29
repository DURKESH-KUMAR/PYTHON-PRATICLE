print("-"*70)
print("\t\t\tcomponent of the car")
print("-"*70)
x=int(input("how much component are you willing to add :"))
y={}
for i in range(1,x+1):
    print("enter the component of the car {}:".format(i))
    a=input("enter the automobile component :")
    b=input("enter the component name :")
    y[a]=b
print("hence the data collected :",y)
print("-"*70)
    
