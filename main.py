import unittest
from tests.test_add_user import TestAddUser

if __name__ == "__main__":
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestAddUser)
    unittest.TextTestRunner().run(test_suite)
