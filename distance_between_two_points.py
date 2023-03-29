print("-"*70)
print("\t\t\tDISTANCE BETWEEN TWO POINTS")
print("-"*70)
print("FOR POINT 1 :")

x=[]
for i in range(2):
    a=int(input("enter the input point 1:"))
    x.append(a)

y=[]
for j in range(2):
    b=int(input("enter the input point 2:"))
    y.append(b)
print("point 1 :",x)
print("point 2 :",y)
print("-"*70)
print("distance between two points :")
x1=x[0]
x2=x[1]
y1=y[0]
y2=y[1]

z=(((x2-x1)**2+(y2-y1)**2)**0.5)
print("the distance between the two points :",z,"meters")
