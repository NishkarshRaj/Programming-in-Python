class InvalidString(Exception):
    def __init__(self,msg):
        self.msg = msg
    def print_exception(self):
        print("Invalid String Exception:",self.msg)

def asteriskChecker(mymessage):
    try:
        flag = 0
        for k in mymessage :
            if k == '*':
                flag = 1
            else:
                pass
        if flag == 1:
            raise InvalidString('Asterisk found!!')
        else:
            pass
    except InvalidString as e:
        e.print_exception()
    else:
        print("String has no Asterisk")
    
message = input("Enter a string: ")
asteriskChecker(message)


