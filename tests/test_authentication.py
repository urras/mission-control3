import unittest
from app.models import User

password = 'thisisatestpass'
wrong_password = 'thisisthewrongpass'

class UserAuthTestCase(unittest.TestCase):

    def test_password_init(self):
        testuser = User(password = password)
        self.assertTrue(testuser.password_hash is not None)

    def test_password_verify(self):
        testuser = User(password = password)
        self.assertTrue(testuser.verify_password(password))
        self.assertFalse(testuser.verify_password(wrong_password))

    def test_password_salt(self):
        testuser = User(password = password)
        testuser2 = User(password = password)
        self.assertFalse(testuser.password_hash == testuser2.password_hash)

