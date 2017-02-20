#test.py

import sys
from nose.tools import *
from Set import *

from src.main import *

def test_calculate():
    eq_(calculate(2, 3), 6, 'The multiplied value is wrong')
    
    #you use eq_ if you know what the outcome should be and ok_ if you just want to know if it gives you an output. the third argument within the parameter is an error message!!

def test_version():
    eq_(sys.version_info[0], 3, 'Python is not version 3')
    
def test_subtract():
    eq_(subtract(4, 2), 3, 'wrong')

