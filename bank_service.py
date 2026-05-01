from data_handler import save_info, update_info


class BankService:
    def __init__(self, account, account_type):
        self.account = account
        self.account_type = account_type

    def deposit(self, amount):
        result = self.account.give(amount)
        if result["status"]:
            save_info(self.account.name, self.account.balance)
        return result

    def withdraw(self, amount):
        result = self.account.take(amount)
        if result["status"]:
            save_info(self.account.name, self.account.balance)
        return result

    def update_balance(self, new_balance):
        self.account.balance = new_balance
        save_info(self.account.name, self.account.balance)
        return self.account.balance

    def update_account(self, new_name, new_password):
        update_info(
            self.account.name,
            self.account.password,
            new_name,
            new_password,
        )
        self.account.name = new_name

    def apply_benefit(self):
        if hasattr(self.account, "apply_benefit"):
            result = self.account.apply_benefit()
            save_info(self.account.name, self.account.balance)
            return result
        return None