print("Project 3: InstaDB Python Connection")
import cx_Oracle
con = cx_Oracle.connect() #ConnectionIP
cur = con.cursor()

acct_id = input("Enter User Id of your account: ")
if cur.execute("select * from Users where userid = :1",(acct_id)) == None:
    print("User ID does not exist in the Database")
else:
    print("Welcome To Insta DB")
    '''1) Max Likes - Which of my pictures (picture ids) has received maximum likes'''
    cur.execute("select pic_id from likes where user_owner = :1 group by pic_id having count(pic_id) = (select max(count(pic_id)) from likes where user_owner = :2 group by pic_id)",(acct_id,acct_id))
    print(cur.fetchall())
    
    '''2) Min Likes - Which of my pictures (picture ids) has received minimum likes'''
    cur.execute("select pic_id from likes where user_owner = :1 and count(pic_id) = (select min(count(pic_id)) from likes where user_owner = :2 group by pic_id) group by pic_id",(acct_id,acct_id))
    print(cur.fetchall())
    
    '''3) Who liked most - who (userid) has liked my pictures most'''
    cur.execute("select liked_by_username from likes where user_owner = :1 group by user_owner having count(liked_by_username) = (select max(count(liked_by_username)) from likes where user_owner = :2 group by user_owner)",(acct_id,acct_id))
    print(cur.fetchall())
                
    '''4) Music pictures - Show all pictures related to Music'''
    cur.execute("select pic_id from tagofgenre where tagname = 'Music'")
    print(cur.fetchall())
                
    '''5) Popular Tag - Which is the name of most popular tag?'''
    cur.execute("select tagname from tagofgenre where count(tagname) = (select max(count(tagname)) group by tagname")
    print(cur.fetchall())
                
    '''6) Most liked user - Whose pictures (userid) have been liked most?'''
    cur.execute("select user_owner from likes where count(user_owner)=(select max(count(user_owner)) group by user_owner) group by user_owner")
    print(cur.fetchall())
                
    '''7) Old Tagging - Tag my pictures older than 3 years old'''
    cur.execute("insert into tagavailable values ('old')")
    cur.execute("select picture_id from picture_details,Users where picture_details.user_posted=Users.username and Users.userid = :1 and picture_details.picture_id =(select picture_id from picture_details,pictures where pictures.filename=picture_details.filename and pictures.date_posted<year(dateadd(year,-3,getdate())))",(acct_id))
    list1 = cur.fetchall()
    list1 = list(list1)
    for k in range (0,len(list1)):
        cur.execute("insert into tagofgenre values ('old',:1)",(list1[k]))
        con.commit()

    '''8) Delete Inactive Users - Delete inactive users i.e. who have been inactive since last 1 year'''
    cur.execute("delete from Users where username = (select username from Users,pictures where Users.username = pictures.username and date_posted < year(dateadd(year,-1,getdate())))")
    con.commit()
                
cur.close()
con.close()
