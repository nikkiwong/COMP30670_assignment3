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
        print(counts)
        expected = np.count_nonzero(LED_Tests.A)
        print(expected)
        self.assertEqual(counts, expected, "Number of lights turned on didn't match")

    def test_TurnOffWorks(self):
        off = Lights.turnOff
        self.assertTrue(off, "Lights didn't turn off")

    def test_SwitchWorks(self):
        sw = Lights.switch
        self.assertTrue(sw, "Lights didn't switch")

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
