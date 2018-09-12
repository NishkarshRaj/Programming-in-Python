class Account:
    def __init__(self, initial_amount):
        self.__balance = initial_amount
    def withdraw(self,amount):
        self.__balance = self.balance - amount
    def deposit(self,amount):
        self.__balance = self.balance + amount
