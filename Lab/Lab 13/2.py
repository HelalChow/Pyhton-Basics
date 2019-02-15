class BankAccount:
    def __init__(self, account_num, balance):
        self.account_num = account_num
        self.balance = balance

    def __repr__(self):
        return "Current balance is "+ str(self.balance)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self,amount):
        if self.balance < amount:
            print("Insufficient Balance. The current balance remained as", self.balance)
        else:
            self.balance -= amount

def main():
    my_account = BankAccount("BOA123", 1000)
    print(my_account)
    my_account.deposit(100)
    print(my_account)
    my_account.withdraw(500)
    print(my_account)
    my_account.withdraw(999999)
    
main()