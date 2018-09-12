print("InfoTech Systems Users")
import cx_Oracle
con = cx_Oracle.connect("system/user123@XE") #Connection IP
cur = con.cursor()

'''1) Create a table "Users" from Python code. '''
statement='''create table Users(
UserId number(10) primary key,
UserName varchar(30) not null,
Password varchar(20) not null,
UserType varchar(20) check (UserType in ('Employer','Jobseeker')))'''
cur.execute(statement)

'''2) Insert data into Users Table using cx_Oracle '''
#2.1) Insert first row using hard-coded values in Insert query
cur.execute("insert into Users values (1,'jobs@infosys.com','jobs@infosys','Employer')")
con.commit()

#2.2) Insert second row using positional bind variables
cur.execute("insert into users values (:v1,:v2,:v3,:v4)",(2,'careers@accenture.com','Acc1','Employer'))
con.commit()

#2.3) Insert third row using named bind variables
cur.execute("insert into users values (:v1,:v2,:v3,:v4)",{"v1":3,"v2":'rahulitsme@gmail.com',"v3":'rahulindia93',"v4":'Jobseeker'})
con.commit()

#2.4) Accept the values for fourth row from user and insert using bind values
print("Enter Details to be inserted in the database")
userid = input("UserID: ") #Enter 4
username = input("UserName: ") #Enter careers@amazon.com
password = input("Password: ") #Enter amazonindia
usertype = input("UserType: ") #Enter Employer
cur.execute("insert into users values (:v1,:v2,:v3,:v4)",{"v1":userid,"v2":username,"v3":password,"v4":usertype})
con.commit()

#2.5) Fetch and display all the records from users table
cur.execute("select * from Users")
print(cur.fetchall())

con.close()
