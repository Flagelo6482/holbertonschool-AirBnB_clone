"""Unittest for class Amenity"""
import unittest
import datetime
from models.amenity import Amenity
from models.base_model import BaseModel


class Test_Amenity(unittest.TestCase):
    """Tests for this class"""

    def test_Amenity(self):
        a1 = Amenity()
        a_dict = a1.to_dict()
        self.assertAlmostEqual(type(a_dict['updated_at']), str)
        self.assertTrue('__class__' in a_dict)
        self.assertAlmostEqual(type(a1.created_at), datetime.datetime)
        self.assertAlmostEqual(type(a1.updated_at), datetime.datetime)
        self.assertAlmostEqual(a1.name, "")
