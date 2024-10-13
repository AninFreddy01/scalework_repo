import unittest
from oob_bank_system import BankAccount

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        #Set up test environment, runs before every test.
        self.account = BankAccount("Godfred", 100)  # Initialize with $100 balance

    def test_get_balance(self):
        #Test if get_balance method returns the correct balance.
        self.assertEqual(self.account.get_balance(), "Your balance is: $100")

    def test_deposit_valid_amount(self):
        #Test deposit method with a valid amount.
        self.account.deposit(50)
        #self.assertTrue(reults) #check if there is a value
        self.assertEqual(self.account.get_balance(), "Your balance is: $150")
    
    def test_withdraw_valid_amount(self):
        #Test withdraw method with a valid amount.
        self.account.withdraw(30)
        self.assertEqual(self.account.get_balance(), "Your balance is: $70")

if __name__ == "__main__":
    unittest.main()

