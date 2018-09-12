#Exercise 5.1 and 5.2 from Book 1

total = 0
count = 0
maximum = None
minimum = None
average = None

while True:
        try:
                x = input("Enter a number: ")
                if x != 'done':
                        x = int(x)
                        total = total + x
                        count = count + 1
                        if maximum is None or maximum < x:
                            maximum = x
                        if minimum is None or minimum > x:
                            minimum = x
                elif x == "done":
                        average = total/count
                        break
                else:
                        x = int(x)
        except:
            print("Invalid Data")
print("Total of numbers entered:",total)
print("Number of entries",count)
print("Average of numbers entered",average)
print("Maximum number:",maximum)
print("Minimum number:",minimum)
