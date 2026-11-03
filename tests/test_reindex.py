import unittest

from app import index


class ReindexTest(unittest.TestCase):
    def test_reindex_replaces_everything(self):
        index.add(99, "stale")
        self.assertEqual(index.reindex([{"id": 1, "name": "Blue Mug"}]), 1)
        self.assertEqual(index.search("stale"), [])
