class bank:
    def __init__(self, account, name, type):
        self.account = account
        self.name = name
        self.type = type
        self.bal = 0

    def show(self):
        print("Account number=", self.account)
        print("Account holder=", self.name)
        print("Account type=", self.type)
        print("Account balanace=", self.bal)

    def deposit(self, deposit):
        self.bal = self.bal + deposit
        return self.bal

    def withdraw(self, withdraw):
        self.bal = self.bal - withdraw
        return self.bal


n = int(input("Enter the Accounter Number:"))
a = (input("Name of the account holder:"))
b = input("Name of the account type:")
o = bank(n, a, b)
o.show()
while (True):
    print("Menu\n")
    print("1.Deposit\n 2.Withdraw\n")
    c = int(input("Enter youir choice"))
    if (c == 1):
        d = int(input("Enter the amount to be deposited;"))
        o.deposit(d)
        o.show()
    elif(c==2):
        d = int(input("Enter the amount to be withdraw: "))
        if (d>o.bal):
            print("Insufficient Balance")
        else:
            o.withdraw(d)
            o.show()
    else:
        exit()

