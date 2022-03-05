class Emp:

  def __init__(self,emp_id,name,salary,address):
     self.emp_id=emp_id
     self.name=name
     self.salary=salary
     self.address=address
 

class Teacher(Emp):
   
  def __init__(self,dept,sub,emp_id,name,salary,address):
     Emp.__init__(self,emp_id,name,salary,address)
     self.dept=dept
     self.sub=sub 
  

  def display(self):
     print(self.dept)
     print(self.sub)
     print(self.emp_id)
     print(self.name)
     print(self.salary)
     print(self.address)
     

ob2=Teacher("MCA","ADS",1,"JOHN",15000,"Villa-10")

#ob1=Emp(1,"raj",15000,"villa10")
ob2.display()

