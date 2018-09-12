accepted_string=input("Enter a string: ")
str1=str() #empty string declaration
"Removing blank spaces in new string"
for x in accepted_string:
    if x==" ":
        continue
    else:
        str1=str1+x
resultant_string=str() #empty string declaration
"Adding even spaced values"
for x in range (0,len(str1)+1):
    if(x%2==0):
        resultant_string=resultant_string+str1[x]
    else:
        continue
print("accepted string: ",accepted_string)
print("resultant string: ",resultant_string)
print("expected string: ",resultant_string[::-1])
