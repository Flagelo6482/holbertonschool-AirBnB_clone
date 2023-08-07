"""Tests for the FileStorage class"""
import unittest
import models
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage


class Test_FileStorage(unittest.TestCase):
    """Test for this class"""

    def test_FileStorage(self):
        f1 = FileStorage()
        self.assertAlmostEqual(f1._FileStorage__file_path, "file.json")
        self.assertIsInstance(f1._FileStorage__objects, dict)

    def test_all(self):
        f2 = FileStorage()
        self.assertAlmostEqual(f2.all(), f2._FileStorage__objects)

    def test_new(self):
        b1 = BaseModel()
        self.assertIn(f"BaseModel.{b1.id}", models.storage.all().keys())

    def test_save(self):
        self.assertRaises(TypeError, models.storage.save, None)

    def test_reload(self):
        bm = BaseModel()
        bm.save()
        self.assertAlmostEqual(os.path.exists("file.json"), True)

        file_path = FileStorage._FileStorage__file_path
        os.remove(file_path)

        models.storage._FileStorage__objects.clear()
        self.assertAlmostEqual(os.path.exists("file.json"), False)
        self.assertAlmostEqual(models.storage.reload(), None)
        self.assertAlmostEqual(len(models.storage._FileStorage__objects), 0)
        models.storage._FileStorage__objects.clear()
        models.storage.new(bm)
        self.assertAlmostEqual(len(models.storage._FileStorage__objects), 1)
        self.assertEqual(models.storage.all(), {f"BaseModel.{bm.id}": bm})
        bm.save()
        self.assertAlmostEqual(os.path.exists("file.json"), True)
        models.storage._FileStorage__objects.clear()
        self.assertAlmostEqual(len(models.storage._FileStorage__objects), 0)
        models.storage.reload()
        self.assertEqual(len(models.storage._FileStorage__objects), 1)
