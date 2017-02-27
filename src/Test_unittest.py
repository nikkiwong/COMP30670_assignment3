from led_file import Lights
import unittest
import numpy as np


class LED_Tests(unittest.TestCase):
    grid = [[False] * 5 for _ in range(5)]
    A = np.array(grid)
    # def setUp(self):
        # self.lights = Lights(a, b, c, d)

    def test_CountMatch(self):
        C = Lights(5).count()
        counts = np.count_nonzero(LED_Tests.A)
        self.assertEqual(C, counts, "The lights on count does not match")
        
    def test_TurnOnWorks(self):
        on = Lights(5).turnOn(2,2,3,4)
        counts = np.count_nonzero(on)
        expected = 6
        self.assertEqual(counts, expected, "Number of lights turned on didn't match")

    def test_TurnOffWorks(self):
        on = Lights(5).turnOn(2,2,3,4)
        print(on)
        off = Lights.turnOff(on, 1,3,2,4)
        counts = np.size(off) - np.count_nonzero(off)
        expected = 25
        self.assertEqual(counts, expected, "Number of lights turned off didn't match")

    def test_SwitchWorks(self):
        on = Lights(5).turnOn(2,2,3,4)
        sw = Lights(5).switch()
        counts = np.size(sw) - np.count_nonzero(sw)
        expected=0
        self.assertEqual(counts, expected, "Number of lights switched didn't match")

#     def test_ReadFileMatch(self):
#         fm = mainfile.read_uri
#         self.assertEqual(fm, 0, "The file wasn't read correctly")
# 
#     def test_ReadFileNotMatch(self):
#         fm = mainfile.read_uri
#         self.assertNotEqual(fm, 0, "The file wasn't read correctly")
# 
#     def test_ReadFileCountMatch(self, ):
#         fm = mainfile.read_uri
#         self.assertEqual(fm, 0, "The final count does not match")
# 
#     def test_ReadFileCountNotMatch(self):
#         fm = mainfile.read_uri
#         self.assertNotEqual(fm, 0, "The final count does not match")

#
def main():
    unittest.main(verbosity=0)


if __name__ == '__main__':
    main()
