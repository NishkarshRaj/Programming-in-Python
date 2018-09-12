print("InfoTech Systems Query")
import cx_Oracle
connection_object = cx_Oracle.connect("system/user123@XE") #Connection IP
cursor_object = connection_object.cursor()

'''1) Retrieve the name and email id of all the "IT" Companies in "Bangalore" '''
cursor_object.execute("select ComapnyName,EmailID from Employer where IndustryType='IT' and City='Bangalore'")
print(cursor_object.fetchall())

'''2) Retrieve the name,mobile number and email id of all the companies in a given city whose Renewal Status is 'Active'. Use positional bind variables. Accept 'city' as an input from the user '''
city = input("Enter the name of the city whose details you want!")
cursor_object.execute("select CompanyName,,EmailID from Employer where City=:1 and RenewalStatus=:2",(city,'Active'))
print("Results shown using positional bind variables in order are:")
print(cursor_object.fetchall())

'''3) Reverse the order of passing the parameters values in above program and observe the output'''
cursor_object.execute("select CompanyName,,EmailId from Employer where City=:1 and RenewalStatus=:2",('Active',city))
print("Results shown using positional bind variables in reverse order are:")
print(cursor_object.fetchall())

'''4) Implement the scenario in question #2 using named bind variables '''
cursor_object.execute("select CompanyName,,EmailID from Employer where City=:city and RenewalStatus=:renew",{"city":city,"renew":"Active"})
print("Results shown using Named bind variables in order are:")
print(cursor_object.fetchall())

'''5) Reverse the order of passing of the bind variable in the above program and observe the output. Are you getting the same result?'''
cursor_object.execute("select CompanyName,,EmailID from Employer where City=:city and RenewalStatus=:renew",{"city":city,"renew":"Active"})
print("Results shown using Named bind variables in reverse order are:")
print(cursor_object.fetchall())

connection_object.close()
