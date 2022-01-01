
a=input("enter the numbers:").split(" ")

lis=map(int,a)
plis=[]
plis=[x for x in lis if x>0]
print("List of Positive Numbers: ")
print(plis)
