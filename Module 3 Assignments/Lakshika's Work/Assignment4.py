print("Bloom Technology Parking Logs")
import sqlite3
con = sqlite3.connect("ass.db") #ConnectionIP
cur = con.cursor()

'''1) Create the following Vehicle Table as part of the application.'''
statements = '''create table Vehicle(Vehicleid number(5) primary key,Vehiclename varchar(10))'''
cur.execute(statements)
con.commit()

'''2) Insert the following records using executemany() function'''
cur.executemany("insert into Vehicle values (:v1,:v2)",[(2001,'Toyota'),(2002,'Maruti'),(2003,'Nissan'),(2004,'Hyundai')])
con.commit()

'''3) Insert two more rows using named bind variables using executemany()'''
cur.executemany("insert into Vehicle values (:v1,:v2)",[{"v1":2006,"v2":'Honda'},{"v1":2007,"v2":'Volkswagen'}])
con.commit()

'''4) Fetch and display all the records from Vehicle table'''
cur.execute("select * from Vehicle")
print(cur.fetchall())

con.close()
                
