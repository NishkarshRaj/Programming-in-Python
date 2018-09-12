print("Prime number programme!!!")
num=int(input("Enter a number: "))
flag=0
for x in range(1,num+1):
    if num%x==0:
        flag=flag+1
    else:
        pass
if(flag==2):
    print("Number is prime")
else:
    print ("Not prime")

    


    
    
