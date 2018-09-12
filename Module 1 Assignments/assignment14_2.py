print("Sum of n natural numbers")
num=int(input("Enter an integer: "))
sum=0
if(num>0):
    for x in range (1,num+1):
        sum=sum+x
    print(("Sum of natural numbers till %d is %d")%(num,sum))
else:
    print("You entered non-natural number")
    

        
