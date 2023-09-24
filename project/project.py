class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        """Deposit the given amount into the account."""
        self.balance += amount

    def withdraw(self, amount):
        """Withdraw the given amount from the account if sufficient funds are available."""
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount

    def get_balance(self):
        """Get the current account balance."""
        return self.balance

def main():
    """Entry point of the program."""
    account = BankAccount(initial_balance=1000)

    # Display the initial balance
    print("Initial Balance:", account.get_balance())

    # Ask the user for deposit amount and deposit
    deposit_amount = float(input("Enter deposit amount: "))
    account.deposit(deposit_amount)
    print("Balance after deposit:", account.get_balance())

    # Ask the user for withdrawal amount and withdraw
    withdrawal_amount = float(input("Enter withdrawal amount: "))
    account.withdraw(withdrawal_amount)
    print("Balance after withdrawal:", account.get_balance())

if __name__ == "__main__":
    main()
