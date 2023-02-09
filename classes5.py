class Account:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, d):
        self.balance += d
        print("ok")
        
    def withdraw(self, w):
        if self.balance >= w:
            self.balance -= w
            print("ok")
        else:
            print("error")

a1 = Account("Smith",100)
print(a1.owner, a1.balance)
a1.deposit(200)
a1.withdraw(50)
a1.withdraw(1000)