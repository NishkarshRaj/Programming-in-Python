#Assignment 5

class Employee:
    def __init__(self,fn,ln,p):  #doubleunderscoresused
        self.first_name = fn
        self.Last_name = ln
        self.Pay = p
        self.Email = fn + '.' + ln + '@company.com' #Inside constructors never use instance variables on RHS 
    def getFullname(self):
        print("Full name of the employee is:",self.first_name+' '+self.Last_name)
    def getEmail(self):
        print("Email of the employee is:",self.Email)
    def getPay(self):
        print("Pay of the employee is:",self.Pay)
        
print("Enter details of Employee!!!")
fname = input("Enter first name of the employee: ")
lname = input("Enter last name of the employee: ")
pay = int(input("Enter pay of the employee: "))

obj1 = Employee(fname,lname,pay)

#Full name of the Employee
print("Lets see the full name!!!")
obj1.getFullname()

#Email of the employee
print("Lets see the email of the employee!!!")
obj1.getEmail()

#Pay of the employee
print("Lets see the pay of the employee")
obj1.getPay()



