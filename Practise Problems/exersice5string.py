#Exercise 5 of Strings!!!

str = "X-DSPAM-Confidence:0.8475"
startpos = str.find(':')
lastpos = str.find(' ',startpos) #suppose a space is there
if lastpos == None:
    strneeded = str[startpos+1:]
else:
    strneeded = str[startpos+1:lastpos]
strneeded = float(strneeded)
print(strneeded)
