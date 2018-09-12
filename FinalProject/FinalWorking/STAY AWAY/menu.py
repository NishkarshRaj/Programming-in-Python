

''' Menu Page for Normal Login '''
def menu():
    print("\t\t\t\t\t\t\tMain Menu Page\n\n")
    print("1) Upcoming Evolvve Events")
    print("2) Recent News and Trends")
    print("3) Give Feedback for Evolvve\n\n")
    inp = int(input("Enter your choice: "))
    if inp == 1:
        print("Upcoming Evolvve Events!!!") #Till Now neither table nor files written!!!
        cur.execute("select * from events")
        for row in cur:
            print(row)
        print("\n\n")
        print("Enter Any event name you want to know more about!!!")
        print("Press 1) To redirect to menu")
        inp1 = input("Enter your choice: ")
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
        print("1) Recent Trends")
        print("2) Artificial Intelligence")
        print("3) Augmented Reality")
        print("4) Big Data")
        print("5) Block Chain")
        print("6) Cloud Computing")
        print("7) Cyber Security")
        print("8) DevOps")
        print("9) IOT")
        print("10) Robotics")
        print("11) Virtual Reality")
        inp2 = int(input("Enter your choice in integer (1,11): "))
        if inp2 >= 1 and inp <=50: #50 is used not 11 because maybe number of files will be increased in the future!!
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
        filename = input("Enter file name you want to keep for your feedback: ")
        file1 = "Support_" + filename + ".txt" #Support files must be stored as Support_filename.txt
        file = open(file1,"w",1)
        input1 = input("Enter Feedback:\n")
        file.write(input1)
        file.close()
        print("Feedback successfully sent!!!")
    else:
        print("Wrong Choice! Please Try again!")
        menu()
    


''' Menu Page for Admin Login '''
def admin_menu():
    print("1) Create new Event")
    print("2) Create new file for recent news and trends!")
    print("3) Register new member for Evolvve") #using membersignup table insertion
    print("4) Read Feedbacks from Users")
    print("5) Register student/groups for upcoming events")
    print("6) Edit Core Committe Details and Members")
    print("7) Visit Homepage\n\n")
    inp = int(input("Enter your choice: "))
    if inp == 1:
        pass
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
        content_name = input("Enter name of the topic: ")
        f1 = open("recent_trend.txt","a",1)
        f2 = "\n" + str(f) + ") " + content_name
        f1.write(f2)
        inp = input("Enter Content\n")
        file_new.write(inp)
        file_new.close()
        file_t = open("flag_trend.txt","w",1)
        file_t.write(str(f))
    elif inp == 3:
        pass
    elif inp == 4:
        pass
    elif inp == 5:
        print("1) Add new members to Core Committee")
        print("2) Update old data")
        inp = int(input("Enter your choice: "))
        if inp == 1:
            print("Following Committee and their members are already enlisted")
            cur.execute("select * from committee_members")
            for row in cur:
                print(row)
            print("Following Positions can be written")
            cur.execute("select * from positions")
            for row in cur:
                print(row)
            comm_name = input("Enter Committee in which member is to be entered: ")
            member_name = input("Enter name of the Club Member who is to be entered: ")
            pos = input("Enter position in which member is to be entered: ")
            try:
                cur.execute("insert into committee_members values(:c,:m,:p)",{"c":comm_name,"m":member_name,"p":pos})
            except sqlite3.DatabaseError as e:
                print("Database Error encountered:",e)
            except:
                print("Runtime Error encountered")
            finally:
                admin_menu()
        elif inp == 2:
            try:
                input1 = input("Enter SQL Statement to carry out the updation/deletion!!!")
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
    elif inp == 6:
        pass
    elif inp == 7:
        homepage()
    else:
        print("Wrong Choice! Please Try Again...")
        admin_menu()

admin_menu()
