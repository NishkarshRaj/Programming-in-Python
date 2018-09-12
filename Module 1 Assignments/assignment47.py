my_string="""Strings are amongst the most popular data types in Python. We can create the strings by enclosing characters in quotes. Python treats single quotes the same as double quotes."""
print("The number of occurences of word string are:",my_string.lower().count("string"))
def count_words(str1):
    list1=str1.split()
    for k in range(0,len(list1)):
        if list1[k].endswith("on")==True:
            print("Occurences of word",list1[k],"with on at end are:",str1.count(list1[k]))
        else:
            continue
    for k in range(0,len(list1)):
        if (list1[k].startswith("on")!=True) and (list1[k].endswith("on")!=True) and (list1[k].find("on")!=(-1)):
            print("Occurences of word",list1[k],"with on in between are:",str1.count(list1[k]))
        else:
            continue
count_words(my_string)
            
            
