print("Variety Retail Store")
flag=0
list=[("Sofa set",20000),("Dining Table",8500),("T.V. Stand",4599),("Cupboard",13920)]
print("List of items available are")
for k in range(0,len(list)):
    print(list[k])
name=input("Enter the name of the item you want to buy: ")
qty=int(input("Enter the amount of items you want to buy: "))
if qty<0:
    print("Quantity cannot be less than zero")
    bill=0
else:
    for k in range(0,len(list)):
        if list[k][0]==name:
            x=list[k][1]
            flag=1
            break
    if flag==0:
        print("Item not available")
        bill=0
    else:
        bill=qty*x
print("Total amount to be paid is",bill)

