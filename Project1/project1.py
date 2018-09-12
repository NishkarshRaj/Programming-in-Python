#Step 1) Import all the libraries required
import random
import string

#Step 2) Create function of Scrambling of word where input argument will be a single word.
def scramble(word):
    if len(word) <= 3: #if length of word is less than 3, it remains unchanged
        return word
    elif word[-1] == "?" or word[-1] == "." or word[-1] == ";" or word[-1] == "," or word[-1] == "!":
        k=list(word[1:-2])
        random.shuffle(k)
        return word[0]+''.join(k)+word[-2]+word[-1]
    else:
        k=list(word[1:-1])
        random.shuffle(k)
        return word[0]+''.join(k)+word[-1]
        
#Step 3) Create a file from which you want to read the content
print("Welcome to the Project 1 in Python Course")
print("Lets Scramble a complete file!!!")
filename = input("Enter name of the file: ") #Using Input we can prompt user to enter the filename
filename = filename+".txt" #Creating Text file as specified
file = open(filename,"w",1) #File name is a string basically and thus can be pre-specified
num = int(input("Enter lines of content you want to write in the file: "))
print("Enter the content now!!!")
for i in range (0,num):
    str1 = input()
    file.write(str1)
    file.write("\n")
file.close()
'''If you have already created the File and don't want to create it again comment or delete everything written above'''

#Step 4) Read The file content and store it as a list of lines
nish = open(filename,"r+")
lines = nish.readlines()
i=0
list1 = [None]*len(lines)
for line in lines:
    list1[i] = line.split()
    i = i+1
nish.close()
    
#Now we have a list containing elements: One line of a file as a list of all words in line
''' Create a file to write the contents into!!!! '''

#Step 5) Create new file with appened file name as 'Scrambled'
filename = filename.split(".") # Splitting File name by comma delimiter
filename1 = filename[0]+"Scrambled."+filename[1] #Appending Scrambled to the filename before .ext
file1 = open(filename1,"w",1)

#Step 6) Write content into scrambed file by randomizing each word by calling function 'scramble' and maintain the spaces and linefeeds
for k in range (0,len(list1)):
    for j in range (0,len(list1[k])):
        file1.write(scramble(list1[k][j]))
        file1.write(" ")
    file1.write("\n")


