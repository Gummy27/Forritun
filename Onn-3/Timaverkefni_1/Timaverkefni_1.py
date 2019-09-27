class Account():
    def __init__(self, name, funds):
        self.name = name
        self.funds = funds

    def credit(self, amount):
        self.funds += amount

    def debit(self, amount):
        if self.funds > amount:
            self.funds -= amount
            return True

        else:
            print('Debit amount exceeded account balance!')
            return False

    def __str__(self):
        return f"{self.name}: {self.funds} kr"


class SavingsAccount(Account):
    def __init__(self, name, funds, interest):
        super().__init__(name, funds)
        self.interest = interest

    def calculateInterest(self):
        return self.funds * self.interest

class CheckingAccount(Account):
    def __init__(self, name, funds, fee):
        super().__init__(name, funds)
        self.fee = fee

    def credit(self, amount):
        super().credit(amount)
        self.funds -= self.fee

    def debit(self, amount):
        if super().debit(amount):
            self.funds -= self.fee

def greinaskil():
    print("====================")


einar = SavingsAccount("Einar", 200000, 0.09)
gabriel = CheckingAccount("Gabríel", 1000000, 90)

greinaskil()
print(einar)
print(einar.calculateInterest())
einar.credit(einar.calculateInterest())
print(einar)

greinaskil()
print(gabriel)
gabriel.debit(100000000)
print(gabriel)

greinaskil()
print(gabriel)
gabriel.debit(1000)
print(gabriel)
gabriel.credit(1000)
print(gabriel)




