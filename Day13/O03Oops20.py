
from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self):
        print("Account")

    @abstractmethod
    def get_balance(self):
        pass


class Savings(Account):

    def get_balance(self):
        print("Balance in the account is ######.##")

    def deposit(self, amt):
        print(f"Amt credited.....{amt}")


class Current(Account):
    def deposit(self, amt):
        print("Amt credited.....")

    def get_balance(self):
        print("Balance in the account is ######.##")


sa = Savings()
sa.deposit(10000)
sa.get_balance()

print("-" * 40)

cur = Current()
