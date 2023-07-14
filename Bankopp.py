class Bank:
    def _init_(self, name):
        self.name = name
        self.accounts = []

    def create_account(self, account_number, account_holder, initial_balance):
        account = Account(account_number, account_holder, initial_balance)
        self.accounts.append(account)

    def deposit(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            account.deposit(amount)
        else:
            print("Account not found.")

    def withdraw(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            account.withdraw(amount)
        else:
            print("Account not found.")

    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None


class Account:
    def _init_(self, account_number, account_holder, initial_balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposit successful. New balance:", self.balance)
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print("Withdrawal successful. New balance:", self.balance)
            else:
                print("Insufficient funds.")
        else:
            print("Invalid withdrawal amount.")


# Example usage:
bank = Bank("My Bank")

# Create accounts
bank.create_account("123456", "John Doe", 1000)
bank.create_account("987654", "Jane Smith", 500)

# Deposit into an account
bank.deposit("123456", 500)

# Withdraw from an account
bank.withdraw("987654", 200)

# Try to withdraw from a non-existent account
bank.withdraw("555555", 1000)
