def is_prime(num):
    flag=0
    for k in range(1,num+1):
        if num%k==0:
            flag=flag+1
        else:
            continue
    if flag==2:
        return True
    else:
        return False
def is_even(num):
    if num%2==0:
        return True
    else:
        return False
    
