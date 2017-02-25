import unittest

class FooTests(unittest.TestCase):

    def setUp(self):
        self.lights = Lights(a, b, c, d)

    def light_status_match(self):
        self.failUnless(False)
        self.failIf(False)

    def test_count(self):
        self.failUnless(False)
        self.failIf(False)

    def test_turnOn(self):
        self.failUnless(False)
        self.failIf(False)

    def test_turnOff(self):
        self.failUnless(False)
        self.failIf(False)

    def test_switch(self):
        self.failUnless(False)
        self.failIf(False)

    def read_file_match(self):
        self.failUnless(False)
        self.failIf(False)

    def test_read_file(self):
        self.failUnless(False)
        self.failIf(False)


def main():
    unittest.main()

if __name__ == '__main__':
    main()
