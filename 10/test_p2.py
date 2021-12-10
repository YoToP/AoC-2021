import unittest
from p2 import solvep2

class test_p1(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(solvep2("10/example1.txt"), 288957,
                         'Solution not ok.')
    def test_up1(self):
        self.assertEqual(solvep2("10/aoc-2021-day10-up1.txt"), 14841,
                         'Solution not ok.')
    def test_up2(self):
        self.assertEqual(solvep2("10/aoc-2021-day10-up2.txt"), 15282,
                         'Solution not ok.')
    def test_up3(self):
        self.assertEqual(solvep2("10/aoc-2021-day10-up3.txt"), 217388346164004118353258362,
                         'Solution not ok.')
    def test_up4(self):
        self.assertEqual(solvep2("10/aoc-2021-day10-up4.txt"), 187232,
                         'Solution not ok.')
if __name__ == '__main__':
    unittest.main()
