''' Login Page!!! '''
def login():
    try:
        print("\n\n")
        print("\t\t\t\t\t\t\tEvolvve: Student Chapter Application\n\n\n")
        sapid = input("Enter SAP ID: ")
        cur.execute("select password from membersignup where sapid = :sap",{"sap":sapid,})
        pass_database = cur.fetchall()
        if pass_database == None:
            print("User does not exist in Database!!!") #Case 1) User does not exists
            homepage()
        else:
            password = input("Enter Password: ")
            if password == pass_database:
                pass # Case 2: Correct SAP id and password: Grant Access!!! will create menu function later!!!
            else:
                print("Incorrect Password! ")
                print("1) Retry Login")
                print("2) Forgot Password?")
                inp = int(input("Enter your choice [1/2]: "))
                if inp == 1:
                    login() #Case 3: User Exists but types incorrect password!!!
                elif inp == 2:
                    forgotpass(sapid) #Case 4: Users exists but needs to ask password
                else:
                    print("Access Denied! Too much faults!! Redirecting to homepage!")
                    homepage()
    except sqlite3.DatabaseError as e:
        print("Database Error:",e)
    except:
        print("Runtime error encountered!!!")
