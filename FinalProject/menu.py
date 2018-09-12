file_trend = open("flag_trend.txt","r",1)
flag_trend = file_trend.read()
file_trend.close()

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
    inp = int(input("Enter your choice: "))
    if inp == 1:
        pass
    elif inp == 2:
        print("Create new file for recent news and trends!!!")
        print("Current number of files present:",flag_trend)
        f = int(flag_trend)
        f = f + 1
        flag_trend = str(f) + ".txt"
        file_new = open(flag_trend,"w",1)
        inp = input("Enter Content\n")
        file_new.write()
        file_new.close()
        file_t = open("flag_trend.txt","w",1)
        file_t.write(flag_trend)
    elif inp == 3:
        pass
    elif inp == 4:
        pass
    elif inp == 5:
        pass
    elif inp == 6:
        pass
    else:
        print("Wrong Choice! Please Try Again...")
        admin_menu()

admin_menu()
