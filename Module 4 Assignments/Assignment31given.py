def getDiscount(age,gender):
    discount = 0
    if age >= 60:
        if gender == 'F':
            discount = 25
        discount = 20
    elif gender == 'F':
        discount = 15
    return discount

age = int(input("Enter age:"))
gender = input("Enter Gender as M or F:")
discount = getDiscount(age, gender)
print("discount",discount)
