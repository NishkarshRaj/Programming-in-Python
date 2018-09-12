print("Sum of first n natural numbers")
def sum_natural(n):
    sum=0
    for k in range (1,n+1):
        sum=sum+k
    return sum
num=int(input("Enter the number of natural numbers: "))
s=sum_natural(num)
print("The sum of first natural numbers are:",s)
