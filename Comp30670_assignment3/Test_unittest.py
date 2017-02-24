import unittest

class FooTests(unittest.TestCase):

    def setUp(self):
        self.lights = lightOn(a, b, c, d)

    def light_status_match(self):
        self.failUnless(False)
        self.failIf(False)

    def read_file_match(self):
        self.failUnless(False)
        self.failIf(False)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
