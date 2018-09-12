#Assignment 17

''' Parent Class 1: Employee '''
class Employee:
    def __init__(self,salary):
        self._salary = salary #Protected Data Member
    def getSalary(payday,lop):
        pass

''' Parent Class 2: Faculty '''
class Faculty:
    def __init__(self,rem):
        self._remuneration = rem #Protected Data Member
    def teach(course):
        pass

''' Parent Class 3: Visitor '''
class Visitor:
    def __init__(self,rem):
        self.remuneration = rem #Protected Data Member
    def calculateFees(startTime,EndTime):
        pass

''' Child class 1: Clerk -> Inherits Employee '''
class Clerk(Employee):
    def prepareBalancesheet():
        pass

''' Child class 2: RegularFaculty -> Inherits Employee and Faculty '''
class RegularFaculty(Employee,Faculty):
    def prepareBalancesheet():
        pass

''' Child class 3: VisitingFaculty '''
class VisitingFaculty(Visitor,Faculty):
    pass

''' Child class 4: Examiner '''
class Examiner(Visitor):
    def examine():
        pass
