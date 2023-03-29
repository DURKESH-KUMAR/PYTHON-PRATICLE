print("-"*70)
print("\t\t\t zero division error")
print("-"*70)
try:
    x=int(input("enter the data 1:"))
    y=int(input("enter the data 2:"))
    z=x/y
    print("the division of the given data :",z)
except ZeroDivisionError:
    print("no number will divide by zero!!!")
except:
    print("enter the correct input")
finally:
    print("have a good day !!!")
print("-"*70)
