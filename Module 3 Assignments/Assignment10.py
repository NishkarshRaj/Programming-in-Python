#Before executing this program create the table using attached file Assignment10_Table 

#Checking given program for errors
import cx_Oracle
con = cx_Oracle.connect("system/user123@XE") #Connection IP
cur = con.cursor()
try:
    cur.execute("insert into product values ('P106','Jams',150)")
except cx_Oracle.DatabaseError as e:
    print("In except block! Exception encountered!!")
    print("Encountered exception is:",e)
finally:
    print("In finally block")
    con.close()

#Correct code for insertion
con2 = cx_Oracle.connect() #Connection IP
cur = con2.cursor()
try:
    cur.execute("insert into product values ('P106','Jams',150,30)")
except cx_Oracle.DatabaseError as e:
    print("Error encountered is:",e)
finally:
    print("In finally block")
    con2.close()
    
