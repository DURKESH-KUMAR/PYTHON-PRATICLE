print("-"*70)
print("\t\t\treplace the string")
print("-"*70)
x=input("enter the string :")
y=input("enter the modification in this string:")
z=input("enter the updated value of the modified string :")
for i in x:
    if i==y:
        i=z
    print(i,end="")
print(end="\n")
print("-"*70)
