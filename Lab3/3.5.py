class Account:

    def __init__(self, owner, balance):
        self.owner=owner
        self.balance=balance

    def withdraw(self):
        w=int(input())
        if self.balance>=w:
            print("Your balance is:",self.balance-w)
            self.balance=self.balance-w
        else:
            print("Not enough funds")

    def deposit(self):
        d=int(input())
        print("Your balance is", self.balance+d)
        self.balance=self.balance+d


owner=input("Your name:")
balance=int(input("Your balance:"))
z=True
Person=Account(owner, balance)

while z:
    s=input(owner +" ,choose operation, withdraw or deposit, or exit:")
    if s=="withdraw":
        Person.withdraw()
    elif s=="deposit":
        Person.deposit()
    elif s=="exit":
        print("You left")
        z=False
    else:
        print("There is no such operation")