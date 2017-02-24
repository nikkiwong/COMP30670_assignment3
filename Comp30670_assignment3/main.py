import urllib.request
help(urllib.request.urlopen)

def read_file():
    '''use readlines to read a line at a time'''
    filename = "\/assignment_3\/testfile.txt"
    buffer = open(filename).read()

    for line in buffer.split('\n'):
        values = line.strip().split()

#request
    uri = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt"
    req = urllib.request.urlopen(uri)

    buffer = req.read().decode('utf-8')

def read_uri(fname):
    if fname.startswith('http'):
        #use urllib.request.urlopen(uri)
        read_file()
    else:
        #use open(uri)
    return pass





