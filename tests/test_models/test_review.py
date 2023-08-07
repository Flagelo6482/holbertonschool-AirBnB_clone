"""
Unittest for class Review
"""


import unittest
import datetime
from models.review import Review
from models.base_model import BaseModel


class Test_Review(unittest.TestCase):
    """Tests for this class"""

    def test_Review(self):
        r1 = Review()
        r_dict = r1.to_dict()
        self.assertAlmostEqual(type(r_dict['updated_at']), str)
        self.assertTrue('__class__' in r_dict)
        self.assertAlmostEqual(type(r1.created_at), datetime.datetime)
        self.assertAlmostEqual(type(r1.updated_at), datetime.datetime)
        self.assertAlmostEqual(r1.place_id, "")
        self.assertAlmostEqual(r1.user_id, "")
        self.assertAlmostEqual(r1.text, "")
