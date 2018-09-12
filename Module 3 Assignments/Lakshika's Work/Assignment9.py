import sqlite3
con = sqlite3.connect("ass.db") #Connection IP
cur = con.cursor()

try:
    '''1) Try to mention incorrect column name and see the result '''
    cur.execute("delete from Users where User_Id = 2")
except sqlite3.DatabaseError as e:
    print("Error due to invalid column name is:",e)
finally:
    print("In Finally Block")
    print("Lets move to the next Task")
con.close()

try:
    '''2) Enter wrong database connection string and check the Error message!!'''
    con = sqlite3.connect("ass1.db") #Please enter wrong connection Id
    print("If this is printed! Connection Id entered was right!!!")
except sqlite3.DatabaseError as e:
    print("Error due to wrong connection string is:",e)
finally:
    print("In Finally Block")
    print("Lets move to the next Task")

try:
    '''3) Enter wrong Table name and check the error!!!'''
    con2 = sqlite3.connect("ass.db") #Enter correct string connection
    cur = con2.cursor()
    cur.execute("delete from Userss where UserId = 2")
except sqlite3.DatabaseError as e:
    print("Error due to wrong table name is:",e)
finally:
    print("In Finally Block")
    
con.close()
con2.close()
