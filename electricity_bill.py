print("-"*70)
print("\t\t\tELECTRICITY BILL GENERATOR")
print("-"*70)
unit=int(input("ENTER THE UNIT OF CURRENT YOU USED :"))

if unit<=100:
    print("AMOUNT YOU NEED TO PAY :",unit*1.5)
    print("-"*70)
elif unit>100 and unit<=200:
    print("AMOUNT YOU NEED TO PAY :",(100*1.5)+((unit-100)*2.5))
    print("-"*70)
elif unit>200 and unit<=300:
    print("AMOUNT YOU NEED TO PAY :",(100*1.5)+(100*2.5)+(unit-200)*4)
    print("-"*70)
elif unit>300 and unit<=350:
    print("AMOUNT YOU NEED TO PAY :",(100*1.5)+(100*2.5)+(100*4)+((unit-300)*5))
    print("-"*70)
else:
    print("AMOUNT YOU NEED TO PAY :15000")
