import unittest

from app import index


class IndexTest(unittest.TestCase):
    def test_search(self):
        index.add(1, "Blue Mug")
        self.assertEqual(index.search("mug"), [1])
