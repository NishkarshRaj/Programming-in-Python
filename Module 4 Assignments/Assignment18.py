#Assignment 18

from abc import ABC, abstractmethod

''' Parent Class Payment '''
class Payment(ABC):
    VAT = 1.15 #15% VAT
    def __init__(self,purchasecost):
        self.purchasecost = purchasecost
    @abstractmethod
    def final_payment(self):
        pass

''' Subclass Cash Payment '''
class Cash(Payment):
    def __init__(self,purchasecost):
        Payment.__init__(self,purchasecost)
    def final_payment(self):
        finalcost = self.purchasecost * Payment.VAT
        return finalcost

''' Subclass Credit Card Payment '''
class Creditcard(Payment):
    processingfee = 1.02
    def __init__(self,purchasecost):
        Payment.__init__(self,purchasecost)
    def final_payment(self):
        finalcost = self.purchasecost * Payment.VAT * Creditcard.processingfee
        return finalcost

''' Payment Function outside class '''
def payshop():
    costprice = int(input("Enter Purchase Cost: "))
    print("Payment Method:")
    print("Press 1: Cash")
    print("Press 2: Credit Card")
    inputmenu = int(input("Enter your Payment Choice: "))
    if inputmenu == 1:
        print("Payment by Cash")
        obj = Cash(costprice)
        sellingprice = obj.final_payment()
        print("The total amount to be paid is:",sellingprice)
    elif inputmenu == 2:
        print("Payment by Creditcard")
        obj = Creditcard(costprice)
        sellingprice = obj.final_payment()
        print("The total amount to be paid is:",sellingprice)
    else:
        print("Wrong Choice! Please try Again")
        payshop()


''' Main Program '''
print("Welcome to our Shop!!!")
payshop()
