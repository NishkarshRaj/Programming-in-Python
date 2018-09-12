try:
    file=open("testfile1.txt","r",1)
    print("1)Read a file")
    s=file.read()
    print(s)
    print("")
    print("")
    print("2) Add backslash\ before every double quote in file contents")
    list1=s.split('"')
    str1=str()
    for k in range (0,len(list1)):
        if k!=len(list1)-1:
            str1=str1+list1[k]+'\\"'
        else:
            str1=str1+list1[k]
    print(str1)
    print("")
    print("")
    print("3) Write it to another file in the same folder")
    file.close()
    file=open("testfile2.txt","w",1)
    file.write(str1)
    print("")
    print("")
    print("4) Write contents of both the files")
    print(str1)
    print(s)
except TypeError:
    print("Type Error found")
except ValueError:
    print("Value Error found")
except IOError:
    print("Input Output Error found")
except:
    print("Other error")
else:
    print("No errors found")
finally:
    print("Task successfully done")
    
