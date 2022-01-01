def fact():
    a=int(input("Enter the number:"))
    f=1
    if a>0:
        for i in range(1,a+1):
            f=f*i
        print("The factorial is:",f)
fact()
