print("Storing text file as dictionary")
file=open("courses.txt","r+")
lines=file.readlines() #takes line by line with linefeed
dict={}
i=0
for line in lines:
    dict[i]=line.strip() #strip removes linefeed
    i=i+1
print(dict)
file.close()


    

