''' Forgot password code '''
''' When Username exists in Membersignup page but user does not remember his/her password '''
def forgotpass(sap_id):
    print("Enter your Registration Number for verification!!!")
    reg_num = input("Enter your registration number: ")
    cur.execute("select registration_num from membersignup where sapid = :sap",{"sap":sap_id,})
    database_rn = cur.fetchall()
    if database_rn == None:
        print("Registration Number does not exist in our Database!!! Access Denied!!!")
        quit()
    elif database_rn == reg_num:
        print("Database Result Match Success!!!")
        cur.execute("select password from membersignup where sapid = :sap",{"sap":sap_id})
        password = cur.fetchall()
        print("Your Password is:",password)
        print("Press Any key to redirect to login page")
        input()
        login()
    else:
        print("Wrong Registration Number Entered!!! Retry")
        forgotpass(sap_id)
