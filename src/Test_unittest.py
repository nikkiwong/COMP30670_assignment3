from led_file import Lights
import main
import unittest


class LED_Tests(unittest.TestCase):
    grid = [[False] * 10 for _ in range(10)]
    # def setUp(self):
        # self.lights = Lights(a, b, c, d)
    def test_GridSize(self):
        gs = Lights(10).create_grid()
        self.assertEqual(gs, LED_Tests.grid, "Grid size don't match")

    def test_LightStatusMatch(self):
        L = Lights.initial_light_status
        self.assertEqual( L, False, "Not all lights are off")

    def test_LightStatusNotMatch(self):
        L = Lights.initial_light_status
        self.assertNotEqual(L, True, "Not all lights are off")

    def test_CountMatch(self):
        C = Lights(10).count()
        counts = sum(row.count(True) for row in LED_Tests.grid)
        self.assertEqual(C, counts, "The lights on count does not match")

    def test_CountNotMatch(self):
        C = Lights(11).count()
        counts = sum(row.count(True) for row in LED_Tests.grid)
        self.assertEqual(C, counts, "The lights on count does not match")

    def test_TurnOnWorks(self):
        on = Lights(10).turnOn()
        # Lon =
        self.assertEqual(on, Lon, "Number of lights turnrf on didn't match")

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
