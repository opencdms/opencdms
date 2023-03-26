import unittest
from opencdms.utils.paths import base_path


class TestPaths(unittest.TestCase):
    def test_get_base_path(self):
        path = base_path()
        self.assertIsNotNone(path)
        self.assertTrue(path.endswith('opencdms'))
