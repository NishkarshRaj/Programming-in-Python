print("Fibonacci Numbers using Recursion")
def FIBO(number):
    sum=0
    if number==0:
        return 0
    elif number==1:
        return 1
    else:
        sum+= FIBO(number-1)+FIBO(number-2)
    return sum
num=int(input("Enter a number to find fibonacci series until given number: "))    
if num<0:
        print("Negative number not allowed")
else:
        s=FIBO(num)
        print(s)
        
