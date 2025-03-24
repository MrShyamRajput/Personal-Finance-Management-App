import unittest
from unittest.mock import MagicMock
from transactions import *

class TestTransactions(unittest.TestCase):

    def setUp(self):
        self.username = "test_user"
        self.mock_db = MagicMock()

    def test_add_transaction(self):
        # Test if the function calls insert_one
        self.mock_db.insert_one = MagicMock()
        add_transaction(self.username)
        self.mock_db.insert_one.assert_called()

   
    def test_update_transaction(self):
        # Test if update_one is called
        self.mock_db.update_one = MagicMock()
        update_transaction(self.username)
        self.mock_db.update_one.assert_called()

    def test_set_budget(self):
        # Test if update_one is called
        self.mock_db.update_one = MagicMock()
        set_budget(self.username)
        self.mock_db.update_one.assert_called()

if __name__ == "__main__":
    unittest.main()