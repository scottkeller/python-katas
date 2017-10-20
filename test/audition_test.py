import unittest
import sys
import os.path

# Import application code here ...
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.audition import it_runs  # noqa


class TestMarkdownPy(unittest.TestCase):

    def test_it_runs(self):
        self.assertTrue(it_runs())


if __name__ == '__main__':
    unittest.main()
