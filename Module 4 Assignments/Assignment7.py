#Assignment 7
'''
class Dog:
    tricks = []
    def __init__(self, name):
        self.name = name
    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
'''

''' The Above code is wrongly written!! Because a class variables store common values and thus it will be difficult to distinguish the UNIQUE features of both dogs '''

#Corrected Code

class Dog:
    def __init__(self,name,tricks):
        self.name = name
        self.tricks = tricks
    def print_details(self):
        print("Name of the dog is:",self.name)
        print("Tricks dog does are:",self.tricks)

dog1 = Dog('Fido','Roll Over')
dog2 = Dog('Buddy','Play Dead')

print("Details of the dogs are!!!")
dog1.print_details()
dog2.print_details()
