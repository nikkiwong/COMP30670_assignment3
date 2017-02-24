#this is where I will write all my test codes

from nose.tools import *
from led_file import *
from setup import read_file

def testing():
    filename =
    buffer = read_file(filename=filename)
    eq_(len(buffer), 0, "The values do not match for the buffer.")

