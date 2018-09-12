cust_details="Hello John, your customer id is j181"
import re
print("1 Find if the customer name is preceded by hello or Hello and mention if yes")
match=re.search("hello |Hello ",cust_details,re.I)
if (match.group()!=None):
    print("The name is preceded by Hello or hello as:",match.group())
else:
    print("Name is not greeted as asked")
print("")
print("")
print("2) Find, if the given string ends with a pattern containing only one alphabet followed by three numbers? If pattern is found, print the searched result")
match=re.search("\D\d{3}",cust_details)
if match.group()!=None:
    print("The query is true and has result:",match.group())
else:
    print("Query is not true")
print("")
print("")
print('''3) Replace the word starting with "j" followed by three numbers to only the number(remove the alphabet).''')
cust_details=re.sub("j181","181",cust_details)
print(cust_details)
print("")
print("")
print('''4) Replace the word starting with "j" followed by three numbers to only the number(remove the alphabet).''')
cust_details=re.sub("id","ID",cust_details)
print(cust_details)
