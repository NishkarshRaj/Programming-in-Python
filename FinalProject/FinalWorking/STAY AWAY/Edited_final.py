''' Importing necessary modules and packages '''
import sqlite3
from random import randint
from os import system,name
from time import sleep

''' Creation of Connection Object in sqllite for Ubuntu '''
con = sqlite3.connect("pro.db") #Connection IP
cur = con.cursor()


''' Function to generate Student Chapter ID '''
def studentID(stu_id):
    s = int(stu_id)
    flag = 0
    random_value =randint(10000,2000+s)
    try:
        
        file = open("chapterid.txt","r",1)
    except:
        print("The File cannot be opened!!!!")
        exit()
    for lines in file:
        lines = lines.strip()
        x = int(lines)
        if x == random_value:
            flag = 1
        elif x == None:
            break
        else:
            continue
    file.close()
    if flag == 1:
        studentID(s)
    elif flag == 0:
        try:
            file1 = open("chapterid.txt","a",1)
            string = str(random_value)+"\n"
            file1.write(string)
            file1.close()
        except:
            print("File error due to writing in elif block!!!")
        else:
            return random_value

	
''' Function for clearing Python Shell '''
def clear():
    if name=='posix':
	_=system('clear')

''' Loading Function '''
def loading():
    for i in range (0,31):
        if i <10:
            print("Connecting To the Database")
        elif i>=10 and i<21:
            if i==10:
                sleep(3)
                clear()
            else:
                print("Inserting Details in The Database")

        else:
            if i==21:
                sleep(3)
                clear()
            else:
                print("Generating Student Chapted ID")

                
''' Function for fee calculation '''
def fee(name):
    print("Hello",name)
    x = name
    print("Following Packages are available!!!")
    print("1) Premium Membership for 500 Rupees - 1 Year")
    print("2) Gold Membership for 1000 Ruppes - 2 Years")
    print("3) Platinum Membership for 2000 Rupees - 4 Years + Tech Magazines")
    inp = int(input("Enter your Choice [1/2/3] :"))
    if inp == 1:
        return 500
    elif inp == 2:
        return 1000
    elif inp == 3:
        return 2000
    else:
        print("Wrong Choice!! Try Again")
        fee(x) 

''' Password Checker '''
def checkpass(password):
    count_small = 0
    count_capital = 0
    count_number = 0
    count_special = 0
    ''' Password must contain 1 small 1 capital letter 1 digit and 1 special character '''
    for ch in password:
        if ord(ch) in range(97,123):
            count_small += 1 #Ascii for small letter 97-122
        elif ord(ch) in range(65,91):
            count_capital += 1 #Ascii for capital letter 65-90
        elif ord(ch) in range(48,58):
            count_number += 1 #Ascii for number 48-57
        else:
            count_special += 1
    #print(count_small)
    #print(count_capital)
    #print(count_special)
    #print(count_number)
    if count_small >= 1 and count_capital >= 1 and count_special >= 1 and count_number >= 1:
        return 1 #If 1 == True Correct pass
    else:
        return 0 #If 2 == False incorrect pass

''' Menu Page for Normal Login '''
def menu():
    print("\t\t\t\t\t\t\tMain Menu Page\n\n")
    print("1) Upcoming Evolvve Events")
    print("2) Recent News and Trends")
    print("3) Give Feedback for Evolvve")
    print("4) Visit Homepage\n\n")
    inp = int(raw_input("Enter your choice: "))
    if inp == 1:
        print("Upcoming Evolvve Events!!!") #Till Now neither table nor files written!!!
        #cur.execute("select * from events")
        #for row in cur:
            #print(row)
        file3 = open("Event_list.txt","r",1)
        print(file3.read())
        print("\n\n")
        print("Enter Any event name you want to know more about!!!")
        print("Press 1) To redirect to menu")
        inp1 = raw_input("Enter your choice: ")
        if int(inp1) == 1:
            menu()
        else:
            try:
                filename = "Event_" + inp1 + ".txt" #Event files should be stored as Event_filename.txt
                file = open(filename,"r",1)
            except:
                print("File does not exists")
            else:
                print(file.read())
            finally:
                print("Could not find the file... Redirecting to Menu Page!!!")
                menu()
    elif inp == 2:
        print("Recent News and Trends!!!") #No tables required!! Files already written!!!
        file_recent = open("recent_trend.txt","r",1)
        print(file_recent.read())
        file_trend = open("flag_trend.txt","r",1)
        flag_trend = file_trend.read()
        file_trend.close()
        inp2 = int(input("Enter your choice in integer: "))
        if inp2 >= 1 and inp2 <= flag_trend:
            try:
                filename = str(inp2) + ".txt"
                file = open(filename,"r",1)
            except:
                print("Sorry! Unable to open file!!!")
            else:
                print(file.read())
            finally:
                menu()
        else:
            print("Wrong Choice!!! Redirecting to Main Menu!!!")
            menu()
    elif inp == 3:
        print("Writing Feedback!!!")
        filename = raw_input("Enter file name you want to keep for your feedback: ")
        file1 = "Support_" + filename + ".txt" #Support files must be stored as Support_filename.txt
        file = open(file1,"w",1)
        input1 = raw_input("Enter Feedback:\n")
        file.write(input1)
        file.close()
        print("Feedback successfully sent!!!")
    elif inp == 4:
        homepage()
    else:
        print("Wrong Choice! Please Try again!")
        menu()
    

''' Forgot password code '''
''' When Username exists in Membersignup page but user does not remember his/her password '''
def forgotpass(sap_id):
    print("Enter your Registration Number for verification!!!")
    reg_num = raw_input("Enter your registration number: ")
    cur.execute("select registration_num from membersignup where sapid = :sap",{"sap":sap_id,})
    d_rn = cur.fetchall()
    data_rn=list(d_rn[0])
    database_rn=str(data_rn[0])
    if database_rn == None:
        print("Registration Number does not exist in our Database!!! Access Denied!!!")
        quit()
    elif database_rn == reg_num:
        print("Database Result Match Success!!!")
        cur.execute("select password from membersignup where sapid = :sap",{"sap":sap_id})
        passwo = cur.fetchall()
        passw=list(passwo[0])
        password=str(passw[0])
        print("Your Password is:",password)
        print("Redirecting to login page")
        clear()
        login()
        

    else:
        print("Wrong Registration Number Entered!!! Retry")
        inp1=raw_input("Enter y/Y to retry")
        if inp1=='y' or inp1=='Y':
            forgotpass(sap_id)
        else:
            print("Redirecting to homepage!!")
            homepage()


''' Login Page '''
def login():
    try:
        print("\n\n")
        print("\t\t\t\t\t\t\tEvolvve: Student Chapter Application\n\n\n")
        print("\t\t\t\t\t\t\t\tLogin Page!!!\n\n")
        sapid = raw_input("Enter SAP ID: ")
        pass_db=cur.execute("select password from membersignup where sapid = :sap",{"sap":sapid,})
        pass_db = cur.fetchall()
        pass_data=list(pass_db[0])
        pass_database=str(pass_data[0])
        if pass_database == None:
            print("User does not exist in Database!!!") #Case 1) User does not exists
            homepage()
        else:
            password = raw_input("Enter Password: ")
            if password == pass_database:
                menu()
            elif pass_database==None:
                print("Cannot Access password from the database!!!")
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


''' Menu Page for Admin Login '''
def admin_menu():
    print("1) Create new Event")
    print("2) Create new file for recent news and trends!")
    print("3) Read Feedbacks from Users")
    print("4) Register student/groups for upcoming events")
    print("5) Edit Core Committe Details and Members")
    print("6) Visit Homepage\n\n")
    inp = int(raw_input("Enter your choice: "))
    if inp == 1:
        print("Create new event!!!")
        name = raw_input("Enter Event Name for new entry :")
        file4 = open("Event_list.txt","a",1)
        w = "\n" + name
        file4.write(w)
        file4.close()
        content = raw_input("Enter Description of the event!!\n")
        filename = "Event_" + name + ".txt"
        file5 = open("filename","w",1)
        file5.write(content)
        file5.close()
        judge = raw_input("Enter name of the judge :")
        money = input("Enter Prize Money :")
        comm = raw_input("Enter name of the committee who is conducting the event : ")
        cur.execute("insert into events values (:name,:judge,:money,:comm)",{"name":name,"judge":judge,"money":money,"comm":comm})
        con.commit()
        print("\n\n\nNew Event Created!!!!!!!!!")
    elif inp == 2:
        print("Create new file for recent news and trends!!!")
        file_trend = open("flag_trend.txt","r",1)
        flag_trend = file_trend.read()
        file_trend.close()
        print("Current number of files present:",flag_trend)
        f = int(flag_trend)
        f = f + 1
        flag_trend = str(f) + ".txt"
        file_new = open(flag_trend,"w",1)
        content_name = raw_input("Enter name of the topic: ")
        f1 = open("recent_trend.txt","a",1)
        f2 = "\n" + str(f) + ") " + content_name
        f1.write(f2)
        inp = raw_input("Enter Content\n")
        file_new.write(inp)
        file_new.close()
        file_t = open("flag_trend.txt","w",1)
        file_t.write(str(f))
    elif inp == 3:
        import os
        print("Available Support Files are:\n")
        for file in os.listdir("F:\Foldername"):#Path has to be inserted here Dont end with \ else unicode problem
            if file.endswith(".txt") and file.startswith("Support_"):
                print(os.path.join(file))
        filename = raw_input("\nEnter the file name of the above list which you want to read\n")
        f = open(filename,'r')
        content = f.read()
        print("\n\nThe Feedback in the file is ")
        print(content)
    elif inp == 5:
        print("1) Add new members to Core Committee")
        print("2) Update old data")
        inp = int(raw_input("Enter your choice: "))
        if inp == 1:
            print("Following Committee and their members are already enlisted")
            cur.execute("select * from committee_members")
            for row in cur:
                print(row)
            print("Following Positions can be written")
            cur.execute("select * from positions")
            for row in cur:
                print(row)
            comm_name = raw_input("Enter Committee in which member is to be entered: ")
            member_name = raw_input("Enter name of the Club Member who is to be entered: ")
            pos = raw_input("Enter position in which member is to be entered: ")
            try:
                cur.execute("insert into committee_members values(:c,:m,:p)",{"c":comm_name,"m":member_name,"p":pos})
                com.commit()
            except sqlite3.DatabaseError as e:
                print("Database Error encountered:",e)
            except:
                print("Runtime Error encountered")
            finally:
                admin_menu()
        elif inp == 2:
            try:
                input1 = raw_input("Enter SQL Statement to carry out the updation/deletion!!!")
                cur.execute(input1)
            except sqlite3.DatabaseError as e:
                print("Database Error encountered:",e)
            except:
                print("Runtime Error Encountered")
            else:
                print("Work Updated Successfully")
            finally:
                admin_menu()
        else:
            print("Wrong Choice! Redirecting to Main Menu")
            admin_menu()
    elif inp == 4:
        print("Registering participants for the Events!!!")
        print("Following Events are available!!!")
        cur.execute("select * from events")
        for row in cur:
            print(cur)
        e_name = raw_input("Enter name of event: ")
        g_name = raw_input("Enter group name :")
        fees = float(raw_input("Enter fees for the group!!!"))
        cur.execute("insert into participation values (:e,:g,:f)",{"e":e_name,"g":g_name,"f":fees})
        print("Now Enter details of the members of the group",g_name)
        inp3 = int(raw_input("Enter Number of participants [1,2,3,4]"))
        if inp3 >=1 and inp3 <=4:
            for i in range(inp3):
                m_name = raw_input("Enter name of the member: ")
                m_sap = raw_input("Enter sapid of the member: ")
                cur.execute("insert into participation members values (:e,:n,:s)",{"e":g_name,"n":m_name,"s":m_sap})
                con.commit()
        else:
            print("Invalid number of participants entered!")
            print("Restart from beginning! Redirecting to Admin menu")
            admin_menu()
    elif inp == 6:
        homepage()
    else:
        print("Wrong Choice! Please Try Again...")
        admin_menu()


''' Login Page '''
def adminlogin():
    try:
        print("\n\n")
        print("\t\t\t\t\t\t\tEvolvve: Student Chapter Application\n\n\n")
        print("\t\t\t\t\t\t\t\tAdmin Login Page\n\n")
        sapid = raw_input("Enter SAP ID: ")
        pass_db=cur.execute("select password from membersignup where sapid = :sap",{"sap":sapid,})
        pass_db = cur.fetchall()
        pass_data=list(pass_db[0])
        pass_database=str(pass_data[0])
        if pass_database == None:
            print("User does not exist in Database!!!") #Case 1) User does not exists
            homepage()
        else:
            password = raw_input("Enter Password: ")
            if password == pass_database:
                print("Successful") # Case 2: Correct SAP id and password: Grant Access!!! will create menu function later!!!
                #Different code from normal login()
                ad_pass = "Evolvve@1"
                admin_pass = raw_input("Enter Admin Password: ")
                if ad_pass == admin_pass:
                    admin_menu()
                else:
                    print("Wrong Admin Password!!")
                    adminlogin()
            elif pass_database==None:
                print("Cannot Access password from the database!!!")
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

        

''' Code For Signup Page '''	
def signup():
    try:
        sleep(8)
        clear()
        print("\t\t\t\t\t\t\t\t\t\tSignUp For Evolvve!\n\n\n")
        name =raw_input("Student Name : ")
        sap_id = raw_input("SAP Id : ")
        password =raw_input("Password : ")
        '''check password function is called '''
        check1 = checkpass(password)
        if check1 == 0:
            print("Error!!!")
            print("Password must contain 1 small letter, 1 capital letter, 1 special character and 1 digit")
            print("Retry!!!")
            x = 1/0
        ''' lets continue forward '''
        roll = raw_input("Registration No. : ")
        branch = raw_input("Branch : ")
        year = int(raw_input("Year Of Study [1/2/3/4] : "))
        gender = raw_input("Gender [M/F/O] : ")
        sleep(3)
        clear()
        loading()
        clear()
        stuchapID = studentID(sap_id)
        fees = fee(name)
        stuchapID = str(stuchapID)
        fees = int(fees)
        cur.execute("insert into membersignup values(:name,:sapid,:pass,:roll,:stuid,:branch,:year,:gender,:memberfee)",{"name":name,"sapid":sap_id,"pass":password,"roll":roll,"stuid":stuchapID,"branch":branch,"year":year,"gender":gender,"memberfee":fees})
        con.commit()
    except sqlite3.DatabaseError as e:
        print("Database Error encountered",e)
    except:
        print("Runtime Error encountered")
    else:
        con.commit()
        clear()
        print("SignUp is successfully completed!!!")
    finally:
        homepage()

''' Homepage of the Application '''
def homepage():
    sleep(4)
    clear()
    print("\t\t\t\t\t\t\t\t\tEvolvve: Student Chapter Application\n\n\n")
    print("\t\t\t1) Login")
    print("\t\t\t2) Admin Login")
    print("\t\t\t3) New User? -> Sign Up")
    print("\t\t\t4) About Evolvve!")
    print("\t\t\t5) Exit Application")
    inp = int(input("Enter your choice: "))
    print("\n\n\n")
    if inp == 1:
        login()
    if inp == 2:
        adminlogin()
    if inp == 3:
        signup()
    if inp == 4:
        about()
    if inp == 5:
        exit()

''' About Evolvve Function using File Handling '''
def about():
    file = open("About.txt","r",1)
    print(file.read())
    input()
    homepage()

homepage()
con.close()
quit()


