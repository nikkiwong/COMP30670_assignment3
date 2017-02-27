import argparse
import sys
import urllib.request
import numpy as np
# help(urllib.request.urlopen)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='input help')
#     parser.add_argument('--kind', help='class type')
    args = parser.parse_args()
    filename = args.input
    
    buffer = read_uri(filename=filename)
#     
#     lines = buffer.split('\n')
#     size = int(lines[0])
#     print(lines)

    newfile = []
    plaintext = buffer.replace(',', ' ')
    for line in plaintext.split('\n'):
        values = line.strip().split()
        if 'through' in values:
            values.remove('through');
        if len(values)>1 and values[0]=='turn':
            values[0:2] = [' '.join(values[0:2])]
        newfile.append(values)     
    A=np.array(newfile)
    print(A)
    
         
def read_uri(filename="input_assign3"):
    if filename.startswith('http'):
        return urllib.request.urlopen(filename).read().decode('utf-8')       
    else:
        return open(filename).read()

if __name__ == '__main__':
    main()

#print('{}{}').__format__(filename, tester.count...
