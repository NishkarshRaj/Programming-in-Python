def getDiscount(age,gender):
    discount = 0
    if age >= 60:
        if gender == 'F' or gender == 'f':
            discount = 25
        elif gender == 'M' or gender == 'm':
            discount = 20
    elif gender == 'F' or gender == 'f':
        discount = 15
    return discount

age = int(input("Enter Age: "))
gender = input("Enter Gender as M or F: ")
discount = getDiscount(age,gender)
print("Discount Percentage is:",discount)
