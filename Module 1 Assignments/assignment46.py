institute="ABC Training Institute"
student_id=(input("Enter the student ID: "))
import re
email_id=str() #empty string declaration
if re.search("^\d+$",student_id):
    student_name=input("Enter name of the Student: ")
    if re.search("^[a-zA-Z]+$",student_name): #Question says only alphabets and thus space is not allowed in check so name can be only one word
        fees_amount=input("Enter the fees to be paid as a number with atmost two precision after decimal: ")
        if re.search("^\d+.\d{2}",fees_amount):
            if fees_amount.count(".")>1:
                print("An amount cannot have more than one period symbol")
            else:
                email_id=student_name+"@ABC.com"            
        else:
            print("Wrong Format for fees")
    else:
        print("Name must have only alphabets in it!!!")
else:
    print("Enter student id only as combination of digits!!")
print("Details of the Student are as follows:")
print("Student ID:",student_id)
print("Student Name:",student_name)
print("Fees Paid:",fees_amount)
print("Email ID:",email_id)
