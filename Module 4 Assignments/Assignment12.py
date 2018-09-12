#Assignment 12

class Calculator:

    currentnum = 1 #for start of program 
    
    #isPrime Function
    @staticmethod
    def isPrime(num):
        count = 0 
        for k in range (1,num+1):
            if num % k == 0:
                count = count + 1
            else:
                pass
            k = k+1
        if count == 2:
            return True
        else:
            return False
        
    #getNextPrime()
    @staticmethod
    def getNextPrime():
        Calculator.currentnum += 1
        while(Calculator.isPrime(Calculator.currentnum)!=True):
            Calculator.currentnum +=1
        return Calculator.currentnum

obj = Calculator()
for k in range (1,51):
    value = obj.getNextPrime()
    print(k,"Prime number is:",value)

    
        
