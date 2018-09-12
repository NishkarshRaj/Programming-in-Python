print("Storing text file as list")
file=open("courses.txt","r+")
lines=file.readlines() #takes line by line with linefeed
list=[None]*len(lines) #what does this line means! why not simple empty list
i=0
for line in lines:
    list[i]=line.strip() #strip removes linefeed
    i=i+1
print(list)
file.close()
