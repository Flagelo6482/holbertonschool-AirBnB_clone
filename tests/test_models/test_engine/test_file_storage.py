"""Test for the FileStorage class"""
import unittest
import models
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class Test_FileStorage(unittest.TestCase):
    """Evidence"""
    def test_FileStorage(self):
        b_1 = FileStorage()
        self.assertAlmostEqual(b_1._FileStorage__file_path, "file.json")
        self.assertIsInstance(b_1._FileStorage__objects, dic)

    def test_all(self):
        b_2 = FileStorage()
        self.assertAlmostEqual(b_2.all(), b_2._FileStorage__objects)

    def test_new(self):
        b_3 = BaseModel()
        self.assertIn(f"BaseModel.{b_3.id}", models.storage.all().keys())

    def test_save(self):
        self.assertRaises(TypeError, models.storage.save, None)

    def test_reload(self):
        b_4 = BaseModel()
        b_4.save()
        self.assertAlmosEqual(os.path.exists("file.json"), True)
        file_path = FileStorage._FileStorage__file_path
        os.remove(file_path)

        models.storage._FileStorage__objects.clear()
        self.assertAlmostEqual(os.path.exists("file.json"), False)
        self.assertAlmostEqual(models.storage.reload(), None)
        self.assertAlmostEqual(len(models.storage._FileStorage__objects), 0)
        models.storage._FileStorage__objects.clear()
        models.storage.new(b_4)
        self.assertAlmostEqual(len(models.storage._FileStorage__objects), 1)
        self.assertEqual(models.storage.all(), {f"BaseModel.{b_4.id}": b_4})
        b_4.save()
        self.assertAlmostEqual(os.path.exists("file.json"), True)
        models.storage._FileStorage__objects.clear()
        self.assertAlmostEqual(len(models.storage._FileStorage__objects), 0)
        models.storage.reload()
        self.assertEqual(len(models.storage._FileStorage__objects), 1)
