def sum_natural(n):
    sum=0
    for k in range (1,n+1):
        sum=sum+k
    return sum
try:
    num=int(input("Enter a natural number until you want to find the sum of natural numbers: "))
except IOError:
    print("Input Output Error")
except TypeError:
    print("Type Error")
except ValueError:
    print("Value Error")
except:
    print("Error")
else:
    print("No errors found")
    s=sum_natural(num)
    print("Sum of first",num,"Natural numbers are:",s)     
