print("Reversing a string using recursion")
def reverse(s):
    if s=="":
        return s
    else:
        return reverse(s[1:])+s[0]
str=input("Enter a string: ")
rstr=reverse(str)
print("The reversed string is:",rstr)
if str==rstr:
    print("The string is palindrome")
else:
    print("The string is not palindrome")
    
