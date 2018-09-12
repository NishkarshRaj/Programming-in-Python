#positive and negative index of string
#While loop traversal of strings!!!!

str1 = input("Enter a string: ")

#forward traversal
index = 0
while index < len(str1):
    print(str1[index])
    index = index + 1

#backward traversal
index = -1
while index >= len(str1)*(-1):
    print(str1[index])
    index = index - 1 
