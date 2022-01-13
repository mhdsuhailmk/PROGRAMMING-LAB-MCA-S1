a=['red','blue','maroon','violet',]
b=['green','magenta','red','violet']
x=[x for x in a if x not in b]
print("a=",a,"b=",b)
print("a-b=",x)
