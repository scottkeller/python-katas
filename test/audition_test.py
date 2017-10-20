import unittest
from src.audition import it_runs


class TestMarkdownPy(unittest.TestCase):

    def test_it_runs(self):
        self.assertTrue(it_runs())


if __name__ == '__main__':
    unittest.main()