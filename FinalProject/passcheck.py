''' Password Checker '''
def checkpass(password):
    count_small = 0
    count_capital = 0
    count_number = 0
    count_special = 0
    ''' Password must contain 1 small 1 capital letter 1 digit and 1 special character '''
    for ch in password:
        if ord(ch) in range(97,123):
            count_small += 1 #Ascii for small letter 97-122
        elif ord(ch) in range(65,91):
            count_capital += 1 #Ascii for capital letter 65-90
        elif ord(ch) in range(48,58):
            count_number += 1 #Ascii for number 48-57
        else:
            count_special += 1
    print(count_small)
    print(count_capital)
    print(count_special)
    print(count_number)
    if count_small >= 1 and count_capital >= 1 and count_special >= 1 and count_number >= 1:
        return 1 #If 1 == True Correct pass
    else:
        return 0 #If 2 == False incorrect pass

password = input("Enter Password: ")
check1 = checkpass(password)
if check1 == 0:
    print("Error!!!")
    print("Password must contain 1 small letter, 1 capital letter, 1 special character and 1 digit")
    print("Retry!!!")
    x = 1/0
    
    
        
        
