def counting(str1,letter):
    counter = 0
    for l in str1:
        if l == letter:
            counter = counter + 1
    return counter

str1 = input("Enter a string: ")
letter = input("Enter a letter whose count you want: ")
counter = counting(str1,letter)
print("Number of letter",letter,"in string",str1,"are:",counter)
