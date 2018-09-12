import random
leave_program='a'
print("This is a program for Dice Throw!!!")
print("Caution! Infinite Loop ahead!!! Type q to quit")
print("Press Enter to continue")
input()
while leave_program != 'q':
    x=random.randint(1,6)
    if x==1:
        print("           ")
        print("           ")
        print("     0     ")
        print("           ")
        print("           ")
        print()
        leave_program=input()
    if x==2:
        print("           ")
        print("           ")
        print("  0     0  ")
        print("           ")
        print("           ")
        print()
        leave_program=input()
    if x==3:
        print("           ")
        print("     0     ")
        print("           ")
        print("  0     0  ")
        print("           ")
        print()
        leave_program=input()
    if x==4:
        print("           ")
        print("  0     0  ")
        print("           ")
        print("  0     0  ")
        print("           ")
        print()
        leave_program=input()
    if x==5:
        print("           ")
        print("  0     0  ")
        print("     0     ")
        print("  0     0  ")
        print("           ")
        print()
        leave_program=input()
    if x==6:
        print("           ")
        print("  0     0  ")
        print("  0     0  ")
        print("  0     0  ")
        print("           ")
        print()
        leave_program=input()
        
    
