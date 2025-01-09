class Ba:
    __accountnumber=1345789      #Use constructor
    __balance=90000
    def show(self):
        print(self.__accountnumber,self.__balance)
    def deposit(self,amount):
        newamount=self.__balance+amount
        print(newamount)
    def withdraw(self,amount):
        remainingbalance=self.__balance-amount
        print(remainingbalance)
obj=Ba()
obj.show()
obj.deposit(500)
obj.withdraw(700)