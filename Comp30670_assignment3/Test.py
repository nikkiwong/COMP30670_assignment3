#this is where I will write all my test codes

from nose.tools import *
from led_file import *
from main import read_file

def testing():
    filename = "C:\Users\Nikki\Desktop\CS UCD\software engineering\/assignment_3\/testfile.txt"
    buffer = read_file(filename == filename)
    eq_(len(buffer), 0, "The values do not match for the buffer...")

def testing_line():
    test =

def tester_run():
    pass

def test_count():
    pass

def test_multi_count():
    pass
