
class Color:
    def __init__(self, R = 0, G = 0, B = 0): #How to initialize. Can set defult values for parameters
        self.R = R
        self.G = G
        self.B = B

    def __repr__(self): #How to return or print values
        return "<" + str(self.R) + ", " + str(self.G) + ", " + str(self.B) + "," + ">"

    def calc_grey_level(self):
        return (self.R + self.B + self.G) //3

class BankAccount:
    def __init__(self, account_num, name, type = "Checking", balance = 0):
        self.account_num = account_num
        self.holder_name = name
        self.account_type = type
        self.balance = balance

    def __repr__(self):
        return "<account #: " + str(self.account_num) + "\n" + "Balance: " + str(self.balance) + ">"

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self,amount):
        if self.balance < amount:
            print("Insufficient Balance")
        else:
            self.balance -= amount

class Bank:
    def __init__(self, name, routing, branch, accounts_filename = None):
        self.name = name
        self.routing_num = routing
        self.branch = branch
        self.accounts = []
        if accounts_filename is not None:
            acc_file = open(accounts_filename, "r")
            acc_file.readline()
            for line in acc_file:
                line = line.rstrip()
                acc_data_list = line.split(',')
                curr_acc = BankAccount(acc_data_list[0], acc_data_list[2])
                self.accounts.append(curr_acc)
    def collect_monthly_fee(self):
        for curr_acc in self.accounts:
            if curr_acc.account_type == "Checking":
                curr_acc.Withdraw(1)
