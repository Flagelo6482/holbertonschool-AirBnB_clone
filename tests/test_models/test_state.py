"""
Unittest for class State
"""


import unittest
import datetime
from models.state import State
from models.base_model import BaseModel


class Test_State(unittest.TestCase):
    """Tests for this class"""

    def test_State(self):
        s1 = State()
        s_dict = s1.to_dict()
        self.assertAlmostEqual(type(s_dict['updated_at']), str)
        self.assertTrue('__class__' in s_dict)
        self.assertAlmostEqual(type(s1.created_at), datetime.datetime)
        self.assertAlmostEqual(type(s1.updated_at), datetime.datetime)
        self.assertAlmostEqual(s1.name, "")
