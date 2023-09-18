class BankAccount:
  def _init_ (self,__accountNumber,__accountHolderName,__initialBalance=0):
    self.__acccountNumber=__accountNumber
    self.__accountHolder=__accountHolderName
    self.__AccountBalance=__initialBalance
    
  def depositMoney(self,amount):
    self.__AccountBalance +=amount
    print("Rs.",amount," has been deposited in your account.")
    
  def withdrawMoney(self,amount):
   if amount>self.__AccountBalance:
     print("insufficient Balance")
   else:
    self.__AccountBalance -=amount
    print("Rs.",amount," has beenwithdrawn from your account")

  def checkBalance(self):
    print("current balance: ",self.__AccountBalance)

obj=BankAccount(123456745,"madhi")
obj.depositMoney(5000)
obj.withdrawMoney(2000)
obj.checkBalance()