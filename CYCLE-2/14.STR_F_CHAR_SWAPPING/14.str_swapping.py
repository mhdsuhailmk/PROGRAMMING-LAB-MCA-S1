f_str=input("Enter the first string:")
s_str=input("Enter the second string:")
temp=f_str[0]
a=f_str.replace(f_str[0],s_str[0])
b=s_str.replace(s_str[0],temp)
print(a ,b)