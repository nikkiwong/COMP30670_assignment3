import argparse
#import urllib.request
#help(urllib.request.urlopen)

# def read_file():
#     '''use readlines to read a line at a time'''
#     filename = "\/assignment_3\/testfile.txt"
#     buffer = open(filename).read()
#
#     for line in buffer.split('\n'):
#         values = line.strip().split()


def read_uri(fname):
    if fname.startswith('http'):
        # request
        #uri = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt"
        req = urllib.request.urlopen(fname)
        buffer = req.read().decode('utf-8')
    else:
        #read_file()
        #fname = "\/assignment_3\/testfile.txt"
        buffer = open(fname).read()

        for line in buffer.split('\n'):
            values = line.strip().split()
    #return


parser = argparse.ArgumentParser(description='a program to count lights turned on')
parser.add_argument('--input', help='input help')
args = parser.parse_args()

filename = args.input


