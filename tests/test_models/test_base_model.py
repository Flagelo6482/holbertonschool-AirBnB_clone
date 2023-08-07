"""
Unittest for class base
"""


import unittest
import datetime
import os
from models.base_model import BaseModel


class Test_BaseModel(unittest.TestCase):
    """Test for this class"""

    def test_BaseModel(self):
        b1 = BaseModel()
        b1_dict = b1.to_dict()
        b2 = BaseModel(**b1_dict)
        self.assertAlmostEqual(type(b1_dict['updated_at']), str)
        self.assertTrue('__class__' in b1_dict)
        self.assertAlmostEqual(type(b1.created_at), datetime.datetime)
        self.assertAlmostEqual(type(b1.updated_at), datetime.datetime)
        self.assertEqual(b1.id, b2.id)
        self.assertEqual(b1.created_at, b2.created_at)
        self.assertEqual(b1.updated_at, b2.updated_at)
        self.assertNotIn('__class__', b2.__dict__)

    def test_str(self):
        b2 = BaseModel()
        self.assertAlmostEqual(type(b2.__str__()), str)

    def test_save(self):
        b3 = BaseModel()
        b_up = b3.updated_at
        b3.save()
        self.assertNotEqual(b_up, b3.updated_at)
        self.assertAlmostEqual(os.path.exists('file.json'), True)

    def test_to_dict(self):
        b4 = BaseModel()
        b4_dict = b4.to_dict()
        self.assertTrue('__class__' in b4_dict)
        self.assertAlmostEqual(type(b4_dict['id']), str)
        self.assertAlmostEqual(type(b4_dict['updated_at']), str)
        self.assertAlmostEqual(type(b4_dict['created_at']), str)
