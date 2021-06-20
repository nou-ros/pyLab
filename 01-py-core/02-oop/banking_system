#abstract class
from abc import ABCMeta, abstractmethod
from random import randint

class Account(metaclass = ABCMeta):
    @abstractmethod
    def create(self, name, balance):
        return 0
    @abstractmethod
    def authenticate(self, name, accNum):
        return 0
    @abstractmethod
    def withdraw(self, withdraw):
        return 0
    @abstractmethod
    def deposit(self, deposit):
        return 0
    @abstractmethod
    def display(self):
        return 0

class Saving(Account):
    def __init__(self):
        #[key][0] => name; [key][1] => balance
        self.accounts={}

    def create(self, name, balance):
        self.accNum = randint(10000,99999)
        self.accounts[self.accNum] = [name, balance]
        print("Account has been created successfully. Your account number is: ", self.accNum)

    def authenticate(self, name, accNum):
        if accNum in self.accounts.keys():
            if self.accounts[accNum][0] == name:
                print("Authentication successful")
                self.accNum = accNum
                return True
            else:
                print("Authentication Failed")
                return False
        
        else: 
            print("Authentication Failed")
            return False
    
    def withdraw(self, withdraw):
        if withdraw > self.accounts[self.accNum][1]:
            print("Insufficient balance")
        else:
            add=self.accounts[self.accNum][1]-withdraw
            self.accounts[self.accNum][1]=add
            print("Withdraw successfull!")
            self.display()
    
    def deposit(self, deposit):
        self.accounts[self.accNum][1] += deposit
        print("Deposition successfull!")
        self.display()

    def display(self):
        print("Available balance: ", self.accounts[self.accNum][1])


one = Saving()

while True:
    print()
    print("Enter 1 to create a new account: ")
    print("Enter 2 to access your accent:  ")
    print("Enter 3 to exit")
    choice = int(input())

    if choice is 1:
        print()
        print("Enter name: ")
        name = input()
        print("Enter your first deposit: ")
        balance = int(input())
        one.create(name, balance)
    
    elif choice is 2:
        print()
        print("Enter your account name: ")
        print()
        name=input()
        print("Enter your account number: ")
        accNum=int(input())
        status = one.authenticate(name, accNum)
        if status is True:
            while True: 
                print()
                print("Enter 1 to withdraw: ")
                print("Enter 2 to deposit: ")
                print("Enter 3 to display balance: ")
                print("Enter 4 to go back to previous menu: ")
                choice = int(input())
                if choice is 1:
                    print()
                    print("Enter withdrawal amount: ")
                    amount = int(input())
                    one.withdraw(amount)
                elif choice is 2:
                    print()
                    print("Enter deposit amount: ")
                    amount = int(input())
                    one.deposit(amount)
                elif choice is 3:
                    print()
                    one.display()
                elif choice is 4: 
                    break

    elif choice is 3:
            quit()

