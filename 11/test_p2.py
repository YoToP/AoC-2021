import unittest
from p2 import solvep2

class test_p1(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(solvep2("11/example1.txt",1000), 195,
                         'Solution not ok.')
    def test_123(self):
        self.assertEqual(solvep2("11/123.txt",1000), 85,
                         'Solution not ok.')
    def test_123extra(self):
        self.assertEqual(solvep2("11/123extra.txt",100000), 83,
                         'Solution not ok.')
    def test_loop(self):
        self.assertEqual(solvep2("11/loop.txt",100000), -1,
                         'Solution not ok.')
if __name__ == '__main__':
    unittest.main()
