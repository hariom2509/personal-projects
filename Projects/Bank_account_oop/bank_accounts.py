class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self,initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(f"\n Account '{self.name}' created \n Balance = ${self.balance:.2f}")

    def getBalance(self):
        print(f"\n Account '{self.name}' Balance = ${self.balance:.2f} ")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("\n Deposit complete.")
        self.getBalance()

    def viableTransaction(self,amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\n Sorry, account {self.name} only has a balance of $ {self.balance:.2f}"
            )
        
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\n withdraw complete.")
            self.getBalance()

        except BalanceException as error:
            print(f"\n withdraw interrupted : {error}")

    def transfer (self, amount , account):
        try:
            print (f"\n ....******\n Beginning transfer .....")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\n transfer complete! ")
        except BalanceException as error:
            print(f"\n transfer interrupted. {error}")
        
