from abc import ABC, abstractmethod
from datetime import datetime


class AbstractBankAccount(ABC):
    @abstractmethod
    def give(self, value):
        pass

    @abstractmethod
    def take(self, value):
        pass


class BankAccount(AbstractBankAccount):
    def __init__(self, name, password, date=None, balance=0):
        self.name = name
        self.__password = password
        self.date = date or datetime.now().strftime("%Y-%m-%d")
        self.__balance = float(balance)
        self.percentage = 0.025

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        self.__balance = float(value)

    @property
    def password(self):
        return self.__password

    def give(self, value):
        if value <= 0:
            return {"status": False, "msg": "Invalid amount"}

        fee = value * self.percentage
        net = value - fee
        self.__balance += net

        return {
            "status": True,
            "net": net,
            "fee": fee,
            "balance": self.__balance,
        }

    def take(self, value):
        if value <= 0:
            return {"status": False, "msg": "Invalid amount"}

        if value > self.__balance:
            return {"status": False, "msg": "Insufficient balance"}

        self.__balance -= value
        return {"status": True, "balance": self.__balance}

    def show_info(self):
        return {
            "name": self.name,
            "type": "Saving" if isinstance(self, SavingAccount) else "Commercial",
            "date": self.date,
            "balance": self.balance,
        }


class SavingAccount(BankAccount):
    def __init__(self, name, password, date=None, balance=0):
        super().__init__(name, password, date, balance)
        self.benefit = 0.02

    def apply_benefit(self):
        bonus = self.balance * self.benefit
        self.balance += bonus
        return {"bonus": bonus, "balance": self.balance}


class CommercialAccount(BankAccount):
    def __init__(self, name, password, date=None, balance=0):
        super().__init__(name, password, date, balance)
        self.range = 0.25

    def take(self, value):
        limit = self.balance + (self.balance * self.range)

        if value > limit:
            return {"status": False, "msg": "Over limit"}

        self.balance -= value
        return {"status": True, "balance": self.balance}