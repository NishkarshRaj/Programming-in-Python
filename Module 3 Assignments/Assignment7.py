import cx_Oracle
con = cx_Oracle.connect("system/user123@XE") #Same connection can be used to access anytable from the current database
cur = con.cursor()
'''1) Delete record of userid = 1 from Users Table '''
cur.execute("delete from Users where UserId = 1")
cur.execute("select * from Users")
print("The new content of table Users is:")
print(cur.fetchall())

'''2) Delete a record from 'Vehicle' table using named bind variables with Vehicleid accepted from user '''
vid = int(input("Enter VehicleId between 1001 to 1007 for Deletion"))
if vid in (1001,1002,1003,1004,1006,1007):
    cur.execute("delete from Vehicle where Vehicleid=:v1",{"v1": vid})
else:
    print("VehicleID not available in Table")
cur.execute("select * from Vehicle")
print("New contents of table Vehicle are:")
print(cur.fetchall())

con.close()
