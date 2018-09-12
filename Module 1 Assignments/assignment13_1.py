print("Retail Store Management Bill")
bill_amount=float(input("Enter the bill amount: "))
flag=0
if (bill_amount>=1000):
    discount = 0.05*bill_amount
elif (bill_amount>=500 and bill_amount<1000):
    discount = 0.02*bill_amount
elif (bill_amount>0 and bill_amount<500):
    discount = 0.01*bill_amount
else:
    flag=1
    print("Please enter positive bill amount")
if flag==0:
    net_amount = bill_amount-discount
    print("The total bill amount after discount is:",net_amount)
print("Thank You for shopping!!!")
    
    
