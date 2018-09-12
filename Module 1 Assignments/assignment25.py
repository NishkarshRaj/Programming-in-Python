print("Variety Retail Store")
dict={"Sofa Set":20000,"Dining Table":8500,"T.V. Stand":4599,"Cupboard":13920}
flag=0
for k in dict:
    print("The items available are")
    print("Item:",k,"is available with base price:",dict[k])
name=input("Enter the name of the item you want to buy: ")
qty=int(input("Enter the quantity of item you want to buy: "))
if qty<0:
    print("Quantity cannot be less than zero")
    bill=0
else:
    for k in dict:
        if k==name:
            x=dict[k]
            flag=1
            break
    if flag==0:
        print("Item is not in the list")
        bill=0
    else:
        bill=dict[k]*qty
print("Total amount to be paid is",bill)
