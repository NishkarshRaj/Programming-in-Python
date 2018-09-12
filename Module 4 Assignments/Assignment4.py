#Assignment 4

class Employee:
    def __init__(self,fn,ln,p):  #doubleunderscoresused
        self.first_name = fn
        self.Last_name = ln
        self.Pay = p
        self.Email = fn + '.' + ln + '@company.com' #Inside constructors never use instance variables on RHS 
    def show_details(self):
        print("First name of the employee is:",self.first_name)
        print("Last name of the employee is:",self.Last_name)
        print("Pay of the employee is:",self.Pay)
        print("Email of the employee is:",self.Email)
        
print("Enter details of Employee!!!")
fname = input("Enter first name of the employee: ")
lname = input("Enter last name of the employee: ")
pay = int(input("Enter pay of the employee: "))

obj1 = Employee(fname,lname,pay)

print("Lets see the details of the Employee!!!")
obj1.show_details()

