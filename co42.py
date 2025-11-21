class BankAccount:
    def __init__(self, no, name, t, bal):
        self.no, self.name, self.t, self.bal = no, name, t, bal

    def deposit(self, a): self.bal += a
    def withdraw(self, a):
        if a <= self.bal: self.bal -= a
        else: print("Insufficient balance")

no = input("Acc No: ")
name = input("Name: ")
t = input("Type: ")
bal = float(input("Balance: "))

acc = BankAccount(no, name, t, bal)

acc.deposit(float(input("Deposit: ")))
acc.withdraw(float(input("Withdraw: ")))

print("Final Balance:", acc.bal)

