from led_file import Lights
import unittest
from main import *
import numpy as np

class LED_Tests(unittest.TestCase):
    
    #sample data that the test codes will run
    testLine1 = "10" " \n turn on 5,5 through 9,9"
    testLine2 = "10" " \n yurn on 0,0 through 9,9"
    testLine3 = "10" " \n turn off 0,0 through 9,9"
    testLine4 = "10" " \n switch 0,0 through 9,9"
    grid = [[False] * 5 for _ in range(5)]
    A = np.array(grid)
    
    def test_parse(self):
        '''This function tests to see if the lines are parsed correctly, 
        if it is parsed correctly there should be 1 in the first sub-array and 5 in the second sub-array'''
        t = parse(LED_Tests.testLine1)
        t = parse(LED_Tests.testLine2)
        t = parse(LED_Tests.testLine3)
        t = parse(LED_Tests.testLine4)
        self.assertEqual(len(t[0][0]), 5, "Didnt parse properly")
        self.assertEqual(len(t[0]), 1, "Didnt parse properly")
        
    def test_read(self):
        '''This function tests to see if the file is read properly by reading the contents of the buffer into a single string , 
        if it the file is read properly the length of the buffer should be equal to 9506'''
        filename = "../data/input_assign3.txt"
        buffer = read_uri(filename=filename)
        self.assertEqual(len(buffer), 9506, "buffer size do not match")
        
    def test_CountMatch(self):
        '''This function tests to see if the function for counting lights turned on works properly, 
        if it the count for lights on is correct then the counts should match'''
        C = Lights(5).count()
        counts = np.count_nonzero(LED_Tests.A)
        self.assertEqual(C, counts, "The lights on count does not match")
        
    def test_TurnOnWorks(self):
        '''This function tests to see if the function for turning on lights works correctly, 
        if it the count for lights on is correct then counts should match the expected'''
        light = Lights(5)
        A = light.turnOn(2,2,3,4)
        counts = np.count_nonzero(A)
        expected = 6
        self.assertEqual(counts, expected, "Number of lights turned on didn't match")

    def test_TurnOffWorks(self):
        '''This function tests to see if the function for turning off lights works correctly, 
        if it the count for lights off is correct then counts should match the expected'''
        light = Lights(5)
        A = light.turnOn(2,2,3,4)
        A = light.turnOff(1,3,2,4)
        counts = np.size(A) - np.count_nonzero(A)
        expected = 21
        self.assertEqual(counts, expected, "Number of lights turned off didn't match")

    def test_SwitchWorks(self):
        '''This function tests to see if the function for switching lights works correctly, 
        if it the count for switched lights is correct then counts should match the expected'''
        light = Lights(5)
        A = light.turnOn(2,2,3,4)
        A = light.switch(1,3,2,4)
        counts = np.count_nonzero(A)
        expected=6
        self.assertEqual(counts, expected, "Number of lights switched didn't match")

def main():
    unittest.main(verbosity=0)


if __name__ == '__main__':
    main()
