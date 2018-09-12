class validation(Exception):
    def __init__(self,msg):
        self.msg = msg
    def print_exception(self):
        print('User Defined Exception found:',self.msg)

try:
    ''' Start Try Block '''
    #1) Age
    age = int(input("Enter your age: "))
    if age >= 0 and age <101:
        pass
    else:
        raise validation("Age is not in given limit 0-100") #1
    #2) Mobile Number
    mobnum = input("Enter your mobile number: ")
    if len(mobnum) == 10:
        for k in mobnum:
            if int(k) >=0 and int(k) <= 9:
                pass
            else:
                raise validation('Invalid character in phone number') #3
    elif len(mobnum) == 11:
        if mobnum[0] == '+':
            for k in range(1,len(mobnum)):
                if int(mobnum[k]) >=0 and int(mobnum[k]) <=9:
                    pass
                else:
                    raise validation('Invalid character in phone number')
        else:
            raise validation('11 Character Phone number must start with +') #4
    else:
        raise validation('Incorrect number length') #4
    #3) Email
    email = input("Enter Email Id: ")
    count_at = 0
    count_period = 0
    for k in email:
        if k == '@':
            count_at += 1
        elif k == '.':
            count_period +=1
        else:
            pass
    if count_at == 1 and count_period >=1:
        pass
    elif count_at != 1:
        raise validation('Incorrect number of @ Symbols used') #5
    else:
        raise validation('Atleast one period must be used!!!') #6
    ''' End Try Block '''
except validation as v:
    v.print_exception()
else:
    print("No errors found!!")
finally:
    print("In Finally Block!!!")
