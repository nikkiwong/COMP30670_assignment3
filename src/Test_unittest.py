from led_file import Lights
import unittest
from main import read_uri
import numpy as np


class LED_Tests(unittest.TestCase):
    grid = [[False] * 5 for _ in range(5)]
    A = np.array(grid)
    # def setUp(self):
        # self.lights = Lights(a, b, c, d)
    def test_read(self):
        filename = "../data/input_assign3.txt"
        buffer = read_uri(filename=filename)
        self.assertEqual(len(buffer), 9506, "buffer size do not match")
        
    def test_CountMatch(self):
        C = Lights(5).count()
        counts = np.count_nonzero(LED_Tests.A)
        self.assertEqual(C, counts, "The lights on count does not match")
        
    def test_TurnOnWorks(self):
        light = Lights(5)
        A = light.turnOn(2,2,3,4)
        counts = np.count_nonzero(A)
        expected = 6
        self.assertEqual(counts, expected, "Number of lights turned on didn't match")

    def test_TurnOffWorks(self):
        light = Lights(5)
        A = light.turnOn(2,2,3,4)
        A = light.turnOff(1,3,2,4)
        counts = np.size(A) - np.count_nonzero(A)
        expected = 21
        self.assertEqual(counts, expected, "Number of lights turned off didn't match")

    def test_SwitchWorks(self):
        light = Lights(5)
        A = light.turnOn(2,2,3,4)
        A = light.switch(1,3,2,4)
        counts = np.count_nonzero(A)
        expected=6
        self.assertEqual(counts, expected, "Number of lights switched didn't match")

 
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
