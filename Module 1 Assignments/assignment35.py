try:
    mylist=[1,2,3,"4",5]
    sum=0
    for i in mylist:
        sum=sum+i
    print(sum)
except:
    print("Value error found")
    mylist[3]=int(mylist[3])
finally:
    sum=0
    for i in mylist:
        sum=sum+i
    print(sum)
try:
    print(mylist[5])
except:
    print("Index max value exceeded. Overflow encountered")
    
