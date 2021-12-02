print("SWAP TWO NUMBRES WITHOUT TEMPORARY VARIABLE")
x=int(input("ENTER THE VALUE OF X:"))
y=int(input("ENTER THE VALUE OF Y:"))
print("BEFORE SWAPPING X:",x,"Y:",y)

x=x+y;
y=x-y;
x=x-y;
print("AFTER SWAPPING . X:",x,"Y:",y)
