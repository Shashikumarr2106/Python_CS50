import unittest
from unittest.mock import patch
from io import StringIO
from project import BankAccount, main

class TestBankAccount(unittest.TestCase):
    def test_deposit(self):
        account = BankAccount(initial_balance=100)
        account.deposit(500)
        self.assertEqual(account.get_balance(), 600)

    def test_withdraw_sufficient_funds(self):
        account = BankAccount(initial_balance=500)
        account.withdraw(200)
        self.assertEqual(account.get_balance(), 300)

    def test_withdraw_insufficient_funds(self):
        account = BankAccount(initial_balance=100)
        account.withdraw(200)
        self.assertEqual(account.get_balance(), 100)  # Balance should remain the same

    def test_get_balance(self):
        account = BankAccount(initial_balance=1000)
        self.assertEqual(account.get_balance(), 1000)

if __name__ == '__main__':
    unittest.main()

