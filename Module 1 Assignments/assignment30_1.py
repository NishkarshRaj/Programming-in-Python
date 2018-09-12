def multiple_3(num,z=1):
    if num==0:
        return
    else:
        print("The",z,"multiple of 3 is:",3*z)
        z=z+1
        multiple_3(num-1,z)
n=int(input("Enter number until which you want multiple of 3: "))
multiple_3(n)
        
