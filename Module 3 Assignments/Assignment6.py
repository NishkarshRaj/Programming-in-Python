import cx_Oracle
con = cx_Oracle.connect("system/user123@XE") #ConnectionIP
cur = con.cursor()

#Function for showing current state of Table Vehicle
def show(cursor):
    cursor.execute("select * from Vehicle")
    i = 1
    for row in cursor:
        print("Content of row number",i,"is:",row)
        i = i+1

'''Update Vehicle Id ranging from 2001-2007 to 1001-1007'''
print("State of table 'Vehilce' before updating Vehicle ID is")
show(cur)
for k in range (2001,2008):
    if k!=2005:
        cur.execute("update Vehicle set Vehicleid = :1 where Vehicleid = :2",(k-1000,k))
    else:
        continue
con.commit()
print("State of table 'Vehicle' after updating Vehicle ID is")
show(cur)

'''Update Vehicle name for VehicleID = 1003 to Mahindra '''
print("State of Table Vehicle before updating Vehcile ID 1003")
show(cur)
cur.execute("update Vehicle set Vehiclename = 'Mahindra' where Vehicleid = 1003")
con.commit()
print("State of Table Vehicle after updating Vehicle ID 1003")
show(cur)

con.close()
    
