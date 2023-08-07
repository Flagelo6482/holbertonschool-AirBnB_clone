"""
Unittest for class City
"""


import unittest
import datetime
from models.city import City
from models.base_model import BaseModel


class Test_City(unittest.TestCase):
    """Tests for this class"""

    def test_City(self):
        c1 = City()
        c_dict = c1.to_dict()
        self.assertAlmostEqual(type(c_dict['updated_at']), str)
        self.assertTrue('__class__' in c_dict)
        self.assertAlmostEqual(type(c1.created_at), datetime.datetime)
        self.assertAlmostEqual(type(c1.updated_at), datetime.datetime)
        self.assertAlmostEqual(c1.state_id, "")
        self.assertAlmostEqual(c1.name, "")
