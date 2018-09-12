import cx_Oracle
con = cx_Oracle.connect("system/user123@XE") #Connection IP
cur = con.cursor()

try:
    '''1) Try to mention incorrect column name and see the result '''
    cur.execute("delete from Users where User_Id = 2")
except cx_Oracle.DatabaseError as e:
    print("Error due to invalid column name is:",e)
finally:
    print("In Finally Block")
    print("Lets move to the next Task")
con.close()

try:
    '''2) Enter wrong database connection string and check the Error message!!'''
    con = cx_Oracle.connect() #Please enter wrong connection Id
    print("If this is printed! Connection Id entered was right!!!")
except cx_Oracle.DatabaseError as e:
    print("Error due to wrong connection string is:",e)
finally:
    print("In Finally Block")
    print("Lets move to the next Task")

try:
    '''3) Enter wrong Table name and check the error!!!'''
    con2 = cx_Oracle.connect() #Enter correct string connection
    cur = con2.cursor()
    cur.execute("delete from Userss where UserId = 2")
except cx_Oracle.DatabaseError as e:
    print("Error due to wrong table name is:",e)
finally:
    print("In Finally Block")
    
con.close()
con2.close()
