''' Class 1: Visitor '''    
class Visitor:
    def __init__(self,name):
        self.__name = name
        self.__visitorId = int()
    def printname(self):
        print(self.__name)

''' Class 2: Employee '''
class Employee:
    def __init__(name,designation):
        self.__empId = int()
        self.__name = name
        self.__designation = designation
    def setDesignation(self,designation):
        self.__designation = designation
    def __str__(self):
        print(self.__empId,":",self.__name,"(",self.__designation,")")

''' Class 3: Course '''
class Course:
    def __init__(self,name):
        self.__courseName = name
    def printname(self):
        print(self.__courseName)

''' Class 4: RegularFaculty '''
class RegularFaculty(Employee):
    def __init__(self,name):
        self.__deptName = name
    def teach(self,course):
        #here sent course is object of class course
        course.printname()

''' Class 5: Department '''
class Department:
    def __init__(self,name):
        self.__deptName = name
        self.__courses = []
        self.__regularFaculties = []
    def addCourse(self,course):
        self.__courses.append(course)
    def addFaculty(self,faculty):
        self.__regularFaculties.append(faculty)

''' Class 6: Institution '''
class Institution:
    def __init__(self,regName,department_count):
        self.__registeredName = regName
        self.__departments = []
        self.__employees = []
        for i in range(0,department_count):
            d = Department(name)
            self.__departments.append(d)
    def event(visitor):
        #Visitor is a object of visitor Uses-a
        visitor.printname()
    def recruit(self,employee):
        #aggregation
        self.__employees.append(employee)


'''Assignment 25 Starts from here '''
d1 = Department("Computer")
e1 = Employee("John","Clerk")
print(e1)
rf1 = RegularFaculty("Jack")
d1.addFaculty(rf1)
e2 = RegularFaculty("Jack",d1,"Professor")
print(e2)
v1 = Visitor("Bill Gates")
inst = Institution("Institute of Technology")
inst.addDepartment(d1)
inst.event(v1)
inst.recruit(e1)
inst.recruit(e2)
c = Courses("Database")
e2.teach(c)

        
    
