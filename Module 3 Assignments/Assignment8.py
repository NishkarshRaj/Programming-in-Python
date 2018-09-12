print("State Banking Organization")
import cx_Oracle
con = cx_Oracle.connect("system/user123@XE") #ConnectionIP
cur = con.cursor()

'''1) Create the table 'Account' as per below specifications'''
cur.execute('''create table Account(
CustomerId number(5) primary key,
AccountNo varchar(15),
AccountType varchar(15) check (AccountType in ('Savings','Current','Recurring')),
Balance number(7)
)''')
con.commit()

'''2) Insertion of the Data'''
cur.executemany("insert into Account values (:v1,:v2,:v3,:v4)",
                [{"v1":101,"v2":'IBI1001',"v3":'Savings',"v4":0},
                 {"v1":102,"v2":'IBI1002',"v3":'Current',"v4":1200},
                 {"v1":103,"v2":'IBI1003',"v3":'Savings',"v4":6543},
                 {"v1":104,"v2":'IBI1004',"v3":'Recurring',"v4":7500},
                 {"v1":105,"v2":'IBI1005',"v3":'Current',"v4":0}
                ])
con.commit()

'''3) Display customer ID and Account balance of the customer with maximum balance'''
cur.execute("select CustomerId,Balance from Account where Balance=(select max(Balance) from Account)")
print("Details of account with Maximum Balance are:",cur.fetchall())

'''4) Fetch the account balance of the customer with customer id 102 and store it in python variable 'acct_bal' '''
cur.execute("select Balance from Account where CustomerId = 102")
acct_balance = cur.fetchall()
print("Account Balance of the Person with Id =102 is:",acct_balance)

'''5) Increment 'acct_balance with 2000 and update the Balance field of same customer to new value'''
acct_balance = list(acct_balance)
acct_balance[0]+=2000
cur.execute("update Account set Balance = :1 where CustomerId = 102",(acct_balance[0]))
con.commit()

'''6) Fetch and observe updated account balance of Customer with CustomerId =102'''
cur.execute("select Balance from Account where CustomerId = 102")
print("The Current Balance of Customer ID =102 is:",cur.fetchall())

'''7) Delete all 'Current' Accounts with Balance = zero'''
cur.execute("delete from Account where Balance = 0 and AccountType = 'Current'")
con.commit()

con.close()
