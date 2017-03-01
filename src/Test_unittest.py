from led_file import Lights
import unittest
from main import *
import numpy as np
import led_file 

class LED_Tests(unittest.TestCase):
    testLine1 = "turn on 5,5 through 9,9"
    testLine2 = "yurn on 0,0 through 9,9"
    testLine3 = "turn off 0,0 through 9,9"
    testLine4 = "switch 0,0 through 9,9"
    grid = [[False] * 5 for _ in range(5)]
    A = np.array(grid)
    def test_parse(self):
        t = parse(LED_Tests.testLine1)
        t = parse(LED_Tests.testLine2)
        t = parse(LED_Tests.testLine3)
        t = parse(LED_Tests.testLine4)
        self.assertEqual(len(t[0][0]), 5, "Didnt parse properly")
    
    def test_execute_cmd(self):
        t = parse(LED_Tests.testLine1)
        print(t)
        x = test_coord(t)
        print(x)
        x = execute_cmd(x)
        print(x)
        
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
