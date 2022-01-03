a=int(input("Enter a number:"))
sum=0
n=a
while a!=0:
    rem=a%10
    sum=sum+(rem*rem*rem)
    a=a//10
	
if(sum==n):
	print("The number is armstrong")
else:
	print("The number is not armstrong")
