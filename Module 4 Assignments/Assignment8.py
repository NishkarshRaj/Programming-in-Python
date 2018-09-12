#Assignment 8

class Employee:
    @classmethod
    def from_string(cls,emp_str):
        #Coded from here
        fn , ln , p = emp_str.split('-')
        return cls(fn,ln,p)
    def __init__(self, first,last,pay):
        self.firstname = first
        self.lastname = last
        self.pay = pay
    def showdetails(self):
        print("Firstname of the employee is:",self.firstname)
        print("Lastname of the employee is:",self.lastname)
        print("Pay of the employee is:",self.pay)

emp_1_str = 'John-Abraham-50000'
emp_1 = Employee.from_string(emp_1_str)
emp_1.showdetails()
