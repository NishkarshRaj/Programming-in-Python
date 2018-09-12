file=open("filehandling_split_for.txt","r")
for line in file:
    tokens=line.split(' ')
    print(tokens)
    print(len(tokens))
file.close()
