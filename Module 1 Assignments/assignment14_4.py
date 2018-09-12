print("Fibonacci Series till nth term")
n=int(input("Enter a number to set range: "))
a,b=0,1
print(b,end=" ")
for x in range(1,n-1):
    c=a+b
    print(c,end=" ")
    a=b
    b=c
print(" ")
print("Thanks for your time")
