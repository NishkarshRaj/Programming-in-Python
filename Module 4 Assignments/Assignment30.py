#Assignment 30
def getDiscount(age):
    discount = 0
    if age > 60 and age < 70:
        discount = 15
    elif age > 70: #must be >=70
        discount = 30
    return discount

myage = int(input("Enter Age: "))
myDiscount = getDiscount(myage)
print("Discount percent =",myDiscount)
