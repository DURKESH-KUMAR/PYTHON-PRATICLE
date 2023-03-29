print("-"*70)
print("\t\t\tnumber of words in a text file")
print("-"*70)
n=input("enter the source file name :")
x=open(n,"r")
n=x.read()
space=0
for i in n:
    if i==" ":
        space+=1
print("number of words in python code :",space)
    
