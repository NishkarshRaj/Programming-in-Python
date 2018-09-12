print("Fibonacci code for lists")
a,b=0,1
z=0
fibb_list=[]
fibb_list.insert(0,a)
fibb_list.insert(1,b)
z=z+1
num=int(input("Enter number of terms in Fibonacci series you want to store: "))
for i in range(0,num-1):
    z=z+1
    fibb_list.insert(z,a+b)
    a=b
    b=fibb_list[z]
for i in range (0,num):
    print(fibb_list[i],end=" ")
    
    
    
