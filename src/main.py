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
    print(A)
    size = int(A[0][0])
    light = Lights(size)
    print(len(A))
    for i in range (1, len(A)-2):
        cmd = A[i][0]
        print(cmd)
        x1 = int(A[i][1])
        print(x1)
        y1 = int(A[i][2])
        print(y1)
        x2 = int(A[i][3])
        print(x2)
        y2 = int(A[i][4])
        print(y2)
        if cmd == 'turn on':
            B = light.turnOn(x1, y1, x2, y2)
        elif cmd == 'turn off':
            B = light.turnOff(x1, y1, x2, y2)
        elif cmd == 'switch':
            B = light.switch(x1, y1, x2, y2)

    return B
    
    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='input help')
#     parser.add_argument('--kind', help='class type')
    args = parser.parse_args()
    filename = args.input
    f = parse(filename)
    print(f)
    print("hello")

if __name__ == '__main__':
    main()

#print('{}{}').__format__(filename, tester.count...
