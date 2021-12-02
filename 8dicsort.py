d={1:100,2:500,3:55,4:56,5:301}
print("BEFORE SORTING:\n",d)
b=sorted(d.items(),key=lambda x:x[1],reverse=True)

a=sorted(d.items(),key=lambda x:x[1])
print("\nASCENDING ORDER=",a,"\nDESCENDING ORDER=",b)
