print("Variety Retail Store")
furniture=['Sofa Set','Dining Table','T.V. Stand','Cupboard']
cost_in_rupees=[20000,8500,4599,13920]
name=input("Enter name of the item you want to buy: ")
amount=int(input("Enter the quantity of the item: "))
flag=0
if amount<0:
    print("Amount cannot be negative!!!")
    bill=0
else:
    for x in range(0,3):
        if furniture[x]==name:
            z=x
            flag=1
    if flag==0:
        print("Item not in the inventory")
        bill=0
    else:
        bill=cost_in_rupees[z]*amount
print("The total bill is:",bill)
