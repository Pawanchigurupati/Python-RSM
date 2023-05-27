class Account:
    def __init__(self, accountNumber, balance):
        self.accountNumber =accountNumber
        self.balance =balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        else:
            print("Insufficient funds ")
            return self.balance

class SavingsAccount(Account):
    def __init__(self, accountNumber, balance, interestRate):
        super().__init__(accountNumber,balance)
        self.interestRate =interestRate

    def calculateInterest(self):
        interest = (self.balance*self.interestRate)/100
        return interest

class CheckingAccount(Account):
    def __init__(self, accountNumber, balance,overdraftLimit):
        super().__init__(accountNumber, balance)
        self.overdraftLimit =overdraftLimit

    def applyOverdraft(self, amount):
        if self.balance-amount<0:
            print("Account is overdrawn")
        elif amount > self.overdraftLimit:
            print("Overdraft limit exceeded")
        else:
            self.balance-=amount
            print("Overdraft applied")
            return self.balance


johnsSavings = SavingsAccount(21563425,564,2.5)
johnsSavings.deposit(500)
johnsSavings.withdraw(200)
interestEarned = johnsSavings.calculateInterest()
print("Interest earned:", interestEarned)

janesChecking = CheckingAccount(34942733,9718,120)
janesChecking.withdraw(300)
janesChecking.applyOverdraft(600)