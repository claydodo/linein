import unittest
from src.linein.source import JSONFolderSource, JSONFileSource


class TestSources(unittest.TestCase):
    def test_JSONFileSource(self):
        source = JSONFileSource('tests/samples/users_to_test_JSONFileSource.json')
        self._test_source(source)

    def test_JSONFolderSource(self):
        source = JSONFolderSource('tests/samples/users_to_test_JSONFolderSource')
        self._test_source(source)

    def _test_source(self, source):
        it = iter(source)
        self.assertDictEqual(next(it), {"username": "alice", "name": "Alice"})
        self.assertDictEqual(next(it), {"username": "bob", "name": "Bob"})
        self.assertDictEqual(next(it), {"username": "carol", "name": "Carol"})
        with self.assertRaises(StopIteration):
            next(it)


