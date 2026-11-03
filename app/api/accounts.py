"""
name: accounts.py
"""

class Account:
    def __init__(self, currency="CAD"):
        self.__currency = currency

    def create_account(self):
        """
        Adds account to accounts table 
        """

