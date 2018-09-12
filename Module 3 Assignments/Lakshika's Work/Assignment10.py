#Before executing this program create the table using attached file Assignment10_Table 

#Checking given program for errors
import sqlite3
con = sqlite3.connect("ass.db") #Connection IP
cur = con.cursor()
try:
    cur.execute("insert into product values ('P106','Jams',150)")
except sqlite3.DatabaseError as e:
    print("In except block! Exception encountered!!")
    print("Encountered exception is:",e)
finally:
    print("In finally block")
    con.close()

#Correct code for insertion
con2 = sqlite3.connect("ass.db") #Connection IP
cur = con2.cursor()
try:
    cur.execute("insert into product values ('P106','Jams',150,30)")
except sqlite3.DatabaseError as e:
    print("Error encountered is:",e)
finally:
    print("In finally block")
    con2.close()
    
