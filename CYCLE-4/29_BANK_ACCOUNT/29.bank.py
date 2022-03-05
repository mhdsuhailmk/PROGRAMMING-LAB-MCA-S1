class Bank:
  def __init__(self):    

    name=input("ENTER THE NAME OF ACCOUNT HOLDER:")
    ac_num=int(input("ENTER THE ACCOUNT NUMBER:"))
    ac_type=input("ENTER THE TYPE OF ACCOUNT:")
    
    self.ac_num=ac_num
    self.name=name
    self.type=ac_type
    self.bal=0

  def deposit(self):
    
    amount=int(input("ENTER THE AMOUNT TO BE DEPOSITED:"))
    self.bal=self.bal+amount
    print("AC_NUM:",self.ac_num)
    print("NAME:",self.name)
    print("TYPE:",self.type)

    print("BALANCE AFTER DEPOSIT:",self.bal)
    

  def withdraw(self):

    amount=int(input("ENTER THE AMOUNT TO BE WITHDRAWN:"))
 
    if self.bal >= amount:
       self.bal=self.bal-amount
       print("AC_NUM:",self.ac_num)
       print("NAME:",self.name)
       print("TYPE:",self.type)
       print("BALANCE AFTER WITHDRAWAL:",self.bal)

    else:
       print("INSUFFICIENT BALANCE")

ob1=Bank()
status=1

while status==1:
    print("1.DEPOSIT","2.WITHDRWAL")
    choice=int(input("ENTER YOUR CHOICE:"))
    
    if choice==1:
      ob1.deposit()

    elif choice==2:
      ob1.withdraw()

    




