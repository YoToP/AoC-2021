import unittest
from p1 import solvep1

class test_p1(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(solvep1("10/example1.txt"), 26397,
                         'Solution not ok.')
    def test_up1(self):
        self.assertEqual(solvep1("10/aoc-2021-day10-up1.txt"), 26448,
                         'Solution not ok.')
    def test_up2(self):
        self.assertEqual(solvep1("10/aoc-2021-day10-up2.txt"), 51474,
                         'Solution not ok.')
    def test_up3(self):
        self.assertEqual(solvep1("10/aoc-2021-day10-up3.txt"), 26340,
                         'Solution not ok.')
    def test_up4(self):
        self.assertEqual(solvep1("10/aoc-2021-day10-up4.txt"), 1314,
                         'Solution not ok.')

if __name__ == '__main__':
    unittest.main()
