class BankAccount:
    def __init__(self,dp,wd):
        self.dp=dp
        self.wd=wd
        print(dp,wd)

    def deposit(self):
        print("The deposited amount is:",self.dp)

    def withdraw(self):
        if(self.deposit==0):
            print("Insufficient Balance")
        else:
            print("The withdrawl amount is:",self.wd)
    def checkbalance(self):
        self.checkbalance=self.dp-self.wd
        print(f"The remaining balance is:{self.checkbalance}")
b=BankAccount(50000,5000)
b.deposit()
b.withdraw()
b.checkbalance()
