import unittest
from calculator import add


class TestAddFunction(unittest.TestCase):
    def test_adding_integers(self):
        self.assertEqual(add(2,2), 4)  # add assertion here


if __name__ == '__main__':
    unittest.main()
