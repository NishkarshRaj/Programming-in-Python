customer_details = {1001:"John",1004:"Jill",1005:"Joe",1003:"Jack"}
flag=0
print("a) Customer Details")
for k in customer_details:
    print("Name of the ",k,"Id customer is",customer_details[k])
print("b) Number of customers")
print("Number of customers are:",len(customer_details))
print("c) Print customer names in ascending order")
import operator
sorted_cust_name=sorted(customer_details.items(),key=operator.itemgetter(1)) #sorted_cust_name is a tuple
for k in range(0,3):
    print(sorted_cust_name[k],end=" ")
print("")    
print("d) Delete the details of customer with customer id=1005 and print updated dictionary")
del customer_details[1005]
for k in customer_details:
    print("Name of the ",k,"Id customer is",customer_details[k])
print('''e) Update the name of customer with customer id = 1003 to "Mary" and print updated dictionary.''')
customer_details[1003]="Mary"
for k in customer_details:
    print("Name of the ",k,"Id customer is",customer_details[k])
print("f) Check whether details of customer with customer id = 1002 exists in the dictionary.")
for k in customer_details:
    if k==1002:
        flag=1
        break
if flag==1:
    print("1002 element record exists in the dictionary")
else:
    print("Record not found")
    
