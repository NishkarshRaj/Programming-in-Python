print("InfoTech Systems Users")
import cx_Oracle
con = cx_Oracle.connect("system/user123@XE") #Connection IP
cur = con.cursor()

def show(cursor): #function to show the current contents of the database
    cursor.execute("select * from Users")
    i = 1
    for row in cursor:
        print("Content of row ",i,"is:",row)
        i = i+1

'''1) Modify the UserName and UserType with UserId=4 such as:
UserName: lookingforjob@yahoo.com
UserType: Jobseeker '''
print("Content of the Table 'Users' before updating values are")
show(cur)
cur.update("update Users set UserName = 'lookingforjob@yahool.com',UserType = Jobseeker where UserId = 4")
print("Content of the Table 'Users' after updating values are")
show(cur)

'''2) Change the password for userid=1. Accept new password from the user during runtime. Fetch and show password for userid = 1 before and after execution of program'''
print("Content of the Table 'Users' before updating values are")
show(cur)
password = input("Enter new password for UserID = 1")
cur.update("update Users set Password = :pass where UserId = 1",(password))
print("Content of the Table 'Users' after updating values are")
show(cur)

con.close()



        
        
