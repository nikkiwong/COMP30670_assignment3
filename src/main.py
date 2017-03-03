import argparse
import urllib.request
import numpy as np
from led_file import *

import time
from _operator import length_hint
from src import led_file

start = time.time()

# help(urllib.request.urlopen) 

def read_uri(filename="input_assign3"):
    
    '''A function to opens and reads a file/url'''
    
    if filename.startswith('http'):
        return urllib.request.urlopen(filename).read().decode('utf-8')       
    else:
        return open(filename).read()
    
def parse(buffer):
    
    '''A function that parses a file, separating and storing them individually into elements in a multidimensional array
    
    It returns an array containing the command and co-ordinates, and a variable containing the size of the grid'''

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

def test_coord(filename):
    
    '''A function to make sure that the co-ordinates are within the grid size given
    
    It returns an array containing the command and co-ordinates, and a variable containing the size of the grid '''
    
    A = filename
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

def execute_cmd(filename):
    
    '''A function that parses the file further into the commands and the axis on the grid for every line and executes 
    those commands appropriately. It also does an error check for spelling mistakes. There are three possible commands,
    therefore if the words do not match, then it moves to the next line.
    
    It returns the count of lights turned on'''
    
    B = filename
    size = B[1]
    A = B[0]
    light = led_file.Lights(size)
    for i in range (0, len(A)-1):
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
    
    
def main():
    
    '''This function executes the functions for parsing the file and executing the commands for the lights
    
    It returns the final count of lights turned on and the time it takes to execute this program'''
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='input help')
    args = parser.parse_args()
    filename = args.input
    buffer = read_uri(filename=filename)
    p = parse(buffer)
    t = test_coord(p)
    f = execute_cmd(t)
    print(f)
    
    end = time.time()
    print(end - start, 'seconds')

if __name__ == '__main__':
    main()
