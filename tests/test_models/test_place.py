"""
Unittest for class Place
"""


import unittest
import datetime
from models.place import Place
from models.base_model import BaseModel


class Test_Place(unittest.TestCase):
    """Tests for this class"""

    def test_Place(self):
        p1 = Place()
        p_dict = p1.to_dict()
        self.assertAlmostEqual(type(p_dict['updated_at']), str)
        self.assertTrue('__class__' in p_dict)
        self.assertAlmostEqual(type(p1.created_at), datetime.datetime)
        self.assertAlmostEqual(type(p1.updated_at), datetime.datetime)
        self.assertAlmostEqual(p1.city_id, "")
        self.assertAlmostEqual(p1.user_id, "")
        self.assertAlmostEqual(p1.name, "")
        self.assertAlmostEqual(p1.description, "")
        self.assertAlmostEqual(p1.number_rooms, 0)
        self.assertAlmostEqual(p1.number_bathrooms, 0)
        self.assertAlmostEqual(p1.max_guest, 0)
        self.assertAlmostEqual(p1.price_by_night, 0)
        self.assertAlmostEqual(p1.latitude, 0.0)
        self.assertAlmostEqual(p1.longitude, 0.0)
        self.assertAlmostEqual(p1.amenity_ids, [])
