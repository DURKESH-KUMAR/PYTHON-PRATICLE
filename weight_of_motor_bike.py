print("-"*70)
print("\t\t\tBIKES LIST ")
print("\t\t* YAMAHA\n\t\t* HONDA\n\t\t* TVS\n\t\t* HERO\n\t\t* ROYAL ENFIELD")
print("-"*70)
print("\t\t\tBIKE CC LIST")
print("\t\t* 125cc\n\t\t* 155cc\n\t\t* 200cc \n\t\t* 350cc")
print("-"*70)
x=input("ENTER THE BIKE NAME :")
cc=int(input("ENTER THE BIKE CC :"))
w1,w2,w3,w4,w5="200 kg","250 kg","300 kg","320 kg","150 kg"
if x=="yamaha" and cc==155:
    print("WEIGHT OF THIS SPECIFIC BIKE :",w1)
elif x=="honda" and cc==125:
    print("WEIGHT OF THIS SPECIFIC BIKE :",w5)
elif x=="tvs" and cc==350:
    print("WEIGHT OF THIS SPECIFIC BIKE :",w4)
elif x=="hero" and cc==125:
    print("WEIGHT OF THIS SPECIFIC BIKE :",w5)
elif x=="royal enfield" and cc==350:
    print("WEIGHT OF THIS SPECIFIC BIKE :",w3)
else:
    print("YOUR INPUT WAS WRONG :")
print("-"*70)
