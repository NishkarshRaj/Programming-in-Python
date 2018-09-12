print("Concatenation of capital letters of two strings in order they appear")
string1=input("Enter a string: ")
string2=input("Enter another string: ")
str1=str()
for x in string1:
    if x.isupper():
        str1=str1+x
for y in string2:
    if y.isupper():
        str1=str1+y
print(string1)
print(string2)
print(str1)
