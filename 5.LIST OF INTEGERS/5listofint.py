s1=0
s2=0
x=[]
n1=input("ENTER THE FIRST LIST:").split(" ")
b=list(map(int,n1))
n2=input("ENTER THE SECOND LIST:").split(" ")
a=list(map(int,n2))
if len(a)==len(b):
    print("LENGTHS ARE EQUAL")
else:
    print("LENGTHS ARE NOT EQUAL")
if sum(a)==sum(b):
    print("SUM OF TWO LISTS ARE EQUAL")
else:
    print("SUM IS DIFFERENT")

print("COMMON VALUES ARE:",end=(" "))
for i in range(0,int(len(a))):
    for j in range(0,int(len(b))):
        if a[i]==b[j]:
            x.append(a[i])

if len(x)==0:
    print("NO COMMON VALUES:")
else:
        print("THE COMMON VALUES ARE:",x)
