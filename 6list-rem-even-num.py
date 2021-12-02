print("PROGRAM TO CREATE A LIST OF INTEGERS WITHOUT EVEN NUMBERS!..")

a=input("ENTR THE NUMBERS")

b= a.split(",")
lis=map(int,b)

new=list()
for i in lis:
	if (i%2)!=0:
	   new.append(i)
	
print(new)
