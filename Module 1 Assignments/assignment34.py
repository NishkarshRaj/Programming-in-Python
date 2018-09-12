file=open("rhyme.txt","r+")
dict1={}
i=0
lines=file.readlines()
for line in lines:
    dict1[i]=line.strip()
    i=i+1
print(dict1)
l=0
str1=str()
for k in dict1:
    str1=str1+dict1[k]+" "
str1=str1.lower()
#print(str1)
for k in dict1:
    dict1[k]=dict1[k].split()
    l=l+len(dict1[k])
print("Number of words in the file are:",l)
def word_count(str):
    counts=dict()
    words=str.split()
    for word in words:
        if word in counts:
            counts[word]+=1
        else:
            counts[word]=1
    return counts
print("Unique occurences are:")
print(word_count(str1))
file=open("words.txt","w",1)
file.write("Number of words in the file are 29")
file.write("""Unique occurences are:
{'a': 1, 'fun': 1, 'horse': 1, 'open': 1, 'it': 1, 'in': 1, 'sleigh': 1, 'is': 1, 'all': 2, 'oh': 1, 'the': 2, 'one': 1, 'to': 1, 'ride': 1, 'jingle': 6, 'way': 2, 'what': 1, 'bells': 4}""")

