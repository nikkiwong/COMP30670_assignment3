import argparse
import urllib.request
import numpy as np
from led_file import Lights
# help(urllib.request.urlopen)

def read_uri(filename="input_assign3"):
    if filename.startswith('http'):
        return urllib.request.urlopen(filename).read().decode('utf-8')       
    else:
        return open(filename).read()
    
def parse(filename):
    buffer = read_uri(filename=filename)

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
    return A

def execute_cmd(filename):
    A = test_coord(filename)
    size = int(A[0][0])
    light = Lights(size)
    for i in range (1, len(A)-1):
        cmd = A[i][0]
        x1 = int(A[i][1])
        y1 = int(A[i][2])
        x2 = int(A[i][3])
        y2 = int(A[i][4])
        if cmd == 'turn on':
            light.turnOn(x1, y1, x2, y2)
        elif cmd == 'turn off':
            light.turnOff(x1, y1, x2, y2)
        elif cmd == 'switch':
            light.switch(x1, y1, x2, y2)

    return light.count()
    
def test_coord(filename):
    coord = parse(filename)
    size = int(coord[0][0])
    for i in range(1, len(coord)):
        if int(coord[i])<0:
            coord[i]=0
        elif int(coord[i])>size:
            coord[i]=size-1
    return coord
    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='input help')
#     parser.add_argument('--kind', help='class type')
    args = parser.parse_args()
    filename = args.input
    f = execute_cmd(filename)
    print(f)

if __name__ == '__main__':
    main()

#print('{}{}').__format__(filename, tester.count...
