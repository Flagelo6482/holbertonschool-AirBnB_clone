"""
Unittest for class User
"""


import unittest
import datetime
from models.user import User
from models.base_model import BaseModel


class Test_User(unittest.TestCase):
    """Tests for this class"""

    def test_User(self):
        u1 = User()
        u_dict = u1.to_dict()
        self.assertAlmostEqual(type(u_dict['updated_at']), str)
        self.assertTrue('__class__' in u_dict)
        self.assertAlmostEqual(type(u1.created_at), datetime.datetime)
        self.assertAlmostEqual(type(u1.updated_at), datetime.datetime)
        self.assertAlmostEqual(u1.email, "")
        self.assertAlmostEqual(u1.password, "")
        self.assertAlmostEqual(u1.first_name, "")
        self.assertAlmostEqual(u1.last_name, "")
