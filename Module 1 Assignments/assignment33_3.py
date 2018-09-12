print("Storing text file as list of dictionary")
file=open("assignment33.txt","r+")
lines=file.readlines() #takes line by line with linefeed
list1=[None]*len(lines) #what does this line means! why not simple empty list
i=0
for line in lines:
    list1[i]=line.strip() #strip removes linefeed
    i=i+1
dict={}
for k in range(0,len(list1)):
    list1[k]=list1[k].split()
    dict[k]={list1[k][0]:list1[k][1]}
    list1[k]=dict[k]
print(list1)
file.close()
