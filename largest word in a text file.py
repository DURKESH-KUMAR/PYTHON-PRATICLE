print("-"*70)
print("\t\t\tlargest word in a text file")
print("-"*70)
x=input("enter the source file:")
n=open(x,"r")
m=n.read()
a=m.split(" ")
print(a)

print("the largest word in a text file is {}".format(max(a)))
print("-"*70)
