try:
    file = open("Assignment27.txt",'r',1)
    content = file.read()
    print(content)
    file.close()
    file = open("Assignment27.txt",'a',1)
    file.write("Hello!")
except TypeError:
    print("Type Error")
except ValueError:
    print("Value Error")
except IOError:
    print("Input Output Error")
except:
    print("Unknown Runtime error")
else:
    print("No Errors Found!!")
finally:
    print("In finally Block!! Always Executed to clean file")
    file.close()
