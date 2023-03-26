import unittest
from opencdms.utils.paths import get_base_path


class TestPaths(unittest.TestCase):
    def test_get_base_path(self):
        base_path = get_base_path()
        self.assertIsNotNone(base_path)
        self.assertTrue(base_path.endswith('opencdms'))
