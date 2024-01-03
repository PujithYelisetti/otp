class BankAccout:
    class BankAccount:
        def __init__(self, accountNumber, name, balance):
            self.accountNumber = accountNumber
            self.name = name
            self.balance = balance

        def deposit(self, amount):
            if amount > 0:
                self.balance += amount
                print(f"Deposit of Rs. {amount} successful")
            else:
                print("Invalid deposit amount.")

        def withdrawal(self, amount):
            if 0 < amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawal of Rs. {amount} successful")
            else:
                print("Invalid withdrawal amount or insuffcient funds")

        def bank_fee(self):
            fees = 0.05 * self.balance
            self.balance -= fees
            print(f"Bank fees of Rs. {fees} applied")

        def display(self):
            print(f"Account Number : {self.accountNumber}")
            print(f"Account Holder : {self.name}")
            print(f"Balance : {self.balance}")

    A1 = BankAccount(accountNumber=1234567, name="Pujith", balance=90000)
    A1.display()
    A1.deposit(10000)
    A1.bank_fee()
    A1.display()
    A1.withdrawal(1016)
    A1.display()