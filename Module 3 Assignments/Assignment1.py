'''1) Connect to Oracle Database '''
import cx_Oracle
connection_object = cx_Oracle.connect("system/user123@XE") #Connection IP
cursor_object = connection_object.cursor()

'''2) Fetch all rows from Table Employee '''
cursor_object.execute("select * from Employer")

'''3) Display all the rows '''
i=1
for row in cursor_object:
    print("Row number",i,"is:",row)
    i = i+1

'''4) Display count of rows fetched '''
cursor_object.fetchall() #Without fetchall() the rowcount attribute does not works
print("The number of rows fetched are:",cursor_object.rowcount)

'''5) Display the description of all the columns of the table'''
print("The table has following Schema:")
print(cursor_object.description)

#Close the Database connection
connection_object.close()
