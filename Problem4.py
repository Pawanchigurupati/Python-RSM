class Account:
    def __init__(self,accountNumber,balance):
        self.accountNumber =accountNumber
        self.balance =balance

class Bank:
    def __init__(self):
        self.accounts =[]
    def addAccount(self,account):
        self.accounts.append(account)
        print("Account",account.accountNumber ,"added to bank")
    def removeAccount(self,accountNumber):
        for account in self.accounts:
            if account.accountNumber ==accountNumber:
                self.accounts.remove(account)
                print("Account", accountNumber ,"removed from bank")
                return
        print("Account", accountNumber ,"not found")
    def calculateBalance(self):
        totalBalance =0
        for account in self.accounts:
            totalBalance+=account.balance
        return totalBalance


account1 =Account("32C54",4343)
account2 =Account("56V45",34523)
account3 =Account("87D65",7698)

myBank =Bank()

myBank.addAccount(account1)
myBank.addAccount(account2)
myBank.addAccount(account3)

totalBalance =myBank.calculateBalance()
print("Total balance in the bank:",totalBalance)

myBank.removeAccount("87D65")

totalBalance =myBank.calculateBalance()
print("Total balance in the bank:",totalBalance)
