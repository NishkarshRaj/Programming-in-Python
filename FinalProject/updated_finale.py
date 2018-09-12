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


