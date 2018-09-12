print("Project 3: InstaDB Python Connection")
import cx_Oracle
import datetime
con = cx_Oracle.connect("system/user@XE") #ConnectionIP
cur = con.cursor()

def options(choice,acct_id):
    if cur.execute("select * from Users where userid =:1",(acct_id,))==None:
        print("User ID does not exist in the Database")
    elif choice=='1':
        print("Welcome To Insta DB")
        '''1) Max Likes - Which of my pictures (picture ids) has received maximum likes'''
        cur.execute("select max(pic_id) from (select pic_id,count(pic_id) from likes where user_owner = :1 group by user_owner)",(acct_id,))
        print(cur.fetchall())
    
    elif choice=='2':
        ''' 2) Min Likes - Which of my pictures (picture ids) has received minimum likes'''
        cur.execute("select min(pic_id) from (select pic_id,count(pic_id) from likes where user_owner = :1 group by user_owner)",(acct_id,))
        print(cur.fetchall())
    
    elif choice=='3':
        '''3) Who liked most - who (userid) has liked my pictures most'''
        cur.execute("select max(user_owner) from (select user_owner,count(user_owner) from likes where pic_id = :1 group by pic_id)",(acct_id,))
        print(cur.fetchall())
                
    elif choice=='4':
        '''4) Music pictures - Show all pictures related to Music'''
        cur.execute("select pic_id from tagofgenre where tagname= 'Music'")
        print(cur.fetchall())

    elif choice=='5':
        '''5) Popular Tag - Which is the name of most popular tag?'''
        cur.execute("select max(tagname) from (select tagname,count(tagname) from likes,tagofgenre where likes.pic_id = tagofgenre.pic_id group by tagofgenre.tagname)")
        print(cur.fetchall())
    
    elif choice=='6':
        '''6) Most liked user - Whose pictures (userid) have been liked most?'''
        cur.execute("select max(user_owner) from (select user_owner,count(user_owner) from likes group by user_owner)")
        print(cur.fetchall())
                
    elif choice=='7':
        '''7) Old Tagging - Tag my pictures older than 3 years old'''
        cur.execute("insert into tagavailable values ('old')")
        cur.execute("select picture_id from picture_details,Users where picture_details.user_posted=Users.username and Users.userid = :1 and picture_details.picture_id =(select picture_id from picture_details,pictures where pictures.filename=picture_details.filename and pictures.date_posted < :2)",(acct_id,year,))
        list1 = cur.fetchall()
        list1 = list(list1)
        for k in range (0,len(list1)):
            cur.execute("insert into tagofgenre values ('old',:1)",(list1[k]))
        
    elif choice=='8':
        '''8) Delete Inactive Users - Delete inactive users i.e. who have been inactive since last 1 year'''
        cur.execute("delete from Users where username = (select u.username from Users u,pictures p where u.username = p.username and p.date_posted < :1)",(year,))
    else:
        print("wrong choice")
ans='n'
print(type(ans))
year = datetime.date.today().strftime("%Y")
acct_id = int(input("Enter User Id of your account: "))
while ans=='n':
    print("1.Max Likes \n2.Min Likes \n3.Who liked most \n4.Music pictures \n5.Popular Tag \n6.Most liked User \n7.Old Taggigng \n8.Delete Inactive Users ")
    choice =raw_input("Enter your choice: ")
    options(choice,acct_id)
    ans=raw_input("Do you Want to exit y\\n? \n")


cur.close()
con.close()
