from led_file import Lights
import mainfile
import unittest


class LED_Tests(unittest.TestCase):

    # def setUp(self):
        # self.lights = Lights(a, b, c, d)

    def test_LightStatusMatch(self):
        L = Lights.initial_light_status
        self.assertEqual( L, 0, "Not all lights are off")

    def test_LightStatusNotMatch(self):
        L = Lights.initial_light_status
        self.assertNotEqual(L, 1, "Not all lights are off")

    def test_CountMatch(self):
        C = Lights.count
        self.assertEqual(C, 0, "The lights on count does not match")

    def test_CountNotMatch(self):
        C = Lights.count
        self.assertEqual(C, 0, "The lights on count does not match")

    def test_TurnOnWorks(self):
        on = Lights.turnOn
        self.assertTrue(on, "Lights didn't turn on")

    def test_TurnOffWorks(self):
        off = Lights.turnOff
        self.assertTrue(off, "Lights didn't turn off")

    def test_SwitchWorks(self):
        sw = Lights.switch
        self.assertTrue(sw, "Lights didn't switch")

    def test_ReadFileMatch(self):
        fm = mainfile.read_uri
        self.assertEqual(fm, 0, "The file wasn't read correctly")

    def test_ReadFileNotMatch(self):
        fm = mainfile.read_uri
        self.assertNotEqual(fm, 0, "The file wasn't read correctly")

    def test_ReadFileCountMatch(self, ):
        fm = mainfile.read_uri
        self.assertEqual(fm, 0, "The final count does not match")

    def test_ReadFileCountNotMatch(self):
        fm = mainfile.read_uri
        self.assertNotEqual(fm, 0, "The final count does not match")

#
def main():
    unittest.main(verbosity=0)


if __name__ == '__main__':
    main()
