import argparse
import urllib.request
import re
import numpy as np
# help(urllib.request.urlopen)

# def read_file():
#     '''use readlines to read a line at a time'''
#     filename = "\/assignment_3\/testfile.txt"
#     buffer = open(filename).read()
#
#     for line in buffer.split('\n'):
#         values = line.strip().split()

def read_file(filename):
#     print(filename)
    newfile = []
    i=0
    buffer = open(filename).read()
    plaintext = buffer.replace(',', ' ')
    for line in plaintext.split('\n'):
        values = line.strip().split()
        newfile.append(values)
    A=np.array(newfile)
    print(A)
        
#     with open(filename, 'r') as data:
#         plaintext = data.read()
#     plaintext = plaintext.replace(',', ' ')
#     print(plaintext)
# #     for line in plaintext.split('\n'):
#     ptxt = plaintext.strip().split()
#     print(ptxt)
    
#         uri = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt"
#         req = urllib.request.urlopen(uri)
#         buffer = req.read().decode('utf-8')
# 
# def read_uri(fname):
#     if fname.startswith('http'):
#         # request
#         urllib.request.urlopen(fname)
#     else:
#         #read_file()        
#         open(fname).read()
# 
#         for line in buffer.split('\n'):
#             values = line.strip().split()
            #put the values into a tuple
    #return

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='a program to count lights turned on')
    parser.add_argument('--input', help='input help')
    args = parser.parse_args()
    filename = args.input
    print(filename)
#     
read_file(filename)

# read_file(filename)
