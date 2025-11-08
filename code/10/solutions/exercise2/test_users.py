import unittest
from util.users import User

class TestUser(unittest.TestCase):

    def setUp(self):
        # This method runs before each test.
        # It is useful to create a clean instance of the class to be tested.
        self.valid_user = User("Mario Rossi", "mario.rossi@email.com")

    def test_init_ok(self):
        self.assertEqual(self.valid_user.name, "Mario Rossi")
        self.assertEqual(self.valid_user.email, "mario.rossi@email.com")
        self.assertFalse(self.valid_user.logged)

    def test_login(self):
        self.valid_user.login()
        self.assertTrue(self.valid_user.logged)

    def test_logout(self):
        self.valid_user.login()
        self.valid_user.logout()
        self.assertFalse(self.valid_user.logged)

    def test_init_empty_values(self):
        with self.assertRaises(ValueError):
            User("", "test@email.com")

        with self.assertRaises(ValueError):
            User("Name", "")

if __name__ == '__main__':
    unittest.main()