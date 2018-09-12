str1=input("Enter a string: ")
for x in range (65,91):
    flag=0
    for y in str1:
        if ord(y.upper())==x:
            flag=flag+1
    if(flag!=0):
        print(flag,chr(x))
        

            
