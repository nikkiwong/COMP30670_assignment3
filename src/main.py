import argparse
import urllib.request
import numpy as np
from led_file import Lights

import time
from _operator import length_hint

start = time.time()

# help(urllib.request.urlopen)

def read_uri(filename="input_assign3"):
    '''A function to opens and reads a file/url'''
    if filename.startswith('http'):
        return urllib.request.urlopen(filename).read().decode('utf-8')       
    else:
        return open(filename).read()
    
def parse(filename):
    '''A function that parses a file, separating and storing them individually into elements in a multidimensional array'''
    buffer = read_uri(filename=filename)

    newfile = []
    line = buffer.replace(',', ' ')
    
    line = line.split('\n')
    size = int(line[0])
    
    for x in line:
        values = x.strip().split()
        if 'through' in values:
            values.remove('through');
        if len(values)>1 and values[0]=='turn':
            values[0:2] = [' '.join(values[0:2])]
        if len(values)==0 or values[0]=='turn on' or values[0]=='turn off' or values[0]=='switch' :
            newfile.append(values)  
    A=np.array(newfile)
    return A, size

def execute_cmd(filename):
    '''A function that parses the file further and executes the commands'''
    B = test_coord(filename)
    size = B[1]
    A = B[0]
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
    '''A function to make sure that the co-ordinates are within the grid size given'''
    A = parse(filename)
    coord = A[0]
    size = A[1]
    for i in range(1, len(coord)-1):
        pts1 = int(coord[i][1])
        pts2 = int(coord[i][2])
        pts3 = int(coord[i][3])
        pts4 = int(coord[i][4])
        if pts1<0:
            pts1=0
        elif pts1>size:
            pts1=size-1
        coord[i][1]=pts1
        if pts2<0:
            pts2=0
        elif pts2>size:
            pts2=size-1
        coord[i][2]=pts2
        if pts3<0:
            pts3=0
        elif pts3>size:
            pts3=size-1
        coord[i][3]=pts3
        if pts4<0:
            pts4=0
        elif pts4>size:
            pts4=size-1
        coord[i][4]=pts4
    return coord, size
    
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

end = time.time()
print(end - start, 'seconds')
#print('{}{}').__format__(filename, tester.count...
    