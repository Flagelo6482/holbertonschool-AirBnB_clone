"""
Unittest
"""

import unittest
import datetime
import os
from models.base_model import BaseModel


class Test_BaseModel(unittest.TestCase):
    """Evidence"""
    def test_BaseModel(self):
        b_1 = BaseModel()
        b_1_dict = b_1.to_dict()
        b_2 = BaseModel(**b_1_dict)
        self.assertAlmostEqual(type(b_1_dict['updated_at']), str)
        self.assertTrue('__class__' in b_1_dict)
        self.assertAlmostEqual(type(b_1.created_at), datetime.datetime)
        self.assertAlmostEqual(type(b_1.updated_at), datetime.datetime)
        self.assertEqual(b_1.id, b_2.id)
        self.assertEqual(b_1.created_at, b_2.created_at)
        self.assertEqual(b_1.updated_at, b_2.updated_at)
        self.assertNotIn('__class__', b2.__dict__)

    def test_str(self):
        b_2 = BaseModel()
        self.assertAlmostEqual(type(b_2.__str__()), str)

    def test_save(self):
        b_3 = BaseModel()
        bak = b_3.updated_at
        b_3.save()
        self.assertNotEqual(bak, b_3.updated_at)
        self.assertAlmostEqual(os.path.exists('file.json'), True)

    def test_to_dict(self):
        b_4 = BaseModel()
        b_4_dict = b_4.to_dict()
        self.assertTrue('__class__' in b_4_dict)
        self.assertAlmostEqual(type(b_4_dict['id']), str)
        self.assertAlmostEqual(type(b_4_dict['created_at']), str)
        self.assertAlmostEqual(type(b_4_dict['updated_at']), str)
