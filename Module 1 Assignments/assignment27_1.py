print("Printing Fibonacci series till nth term")
def print_fibonacci(num):
    a,b=0,1
    print(a,end=" ")
    print(b,end=" ")
    for k in range(1,num-1):
        c=a+b
        print(c,end=" ")
        a=b
        b=c
    print("")
    return
n=int(input("Enter a number of terms until which you want to generate Fibonacci Series: "))
print_fibonacci(n)
      
      
