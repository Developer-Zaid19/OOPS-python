class BankAccount:
    def __init__(self, name):
        self.name = name
        balance = 50000
        self.__balance = balance   # private variable
        print(f"Mr.{self.name} your current balance is {self.__balance}")

    def deposit(self, amount):
        self.amount = amount
        self.__balance  
        print(f"Mr.{self.name} your current balance is {self.__balance} + {self.amount} = {self.__balance + self.amount}")
        self.__balance += self.amount
        
    def withdraw(self, amount):
        self.amount = amount
        self.__balance  
        print(f"Mr.{self.name} your current balance is {self.__balance} - {self.amount} = {self.__balance - self.amount}")
        self.__balance -= self.amount

    def get_balance(self):
        print(self.__balance)

acc = BankAccount("zaid")
acc.deposit(5000)
acc.withdraw(3000)
acc.get_balance() # with this you dont check current balance 
# print(acc.balance) #error
