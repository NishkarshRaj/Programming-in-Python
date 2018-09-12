print("User defined function for greatest number in user input values")
def maximum(a,b,c):
    if (a>b and a>c):
        x=a
    elif (b>a and b>c):
        x=b
    else:
        x=c
    return x
a=int(input("Enter an integer value: "))
b=int(input("Enter an integer value: "))
c=int(input("Enter an integer value: "))
value=maximum(a,b,c)
print("Greatest integer is",value)      

    
