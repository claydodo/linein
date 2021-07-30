from django.test import TestCase
from linein.loader import *


class TestBuiltInLoaders(TestCase):
    def test_Loader(self):
        loader = Loader()
        test_data = {"a": 1, "b": 2}
        self.assertDictEqual(loader.parse(test_data), test_data)

        result = loader.load()
        self.assertIsNone(result)

    def test_NullLoader(self):
        loader = NullLoader()
        result = loader.load()
        self.assertIsNone(result)



