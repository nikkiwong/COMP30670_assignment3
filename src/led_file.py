import numpy as np
 
class Lights:
    
    '''A class containing methods for the Lights'''
    
    def __init__(self, s):
        '''takes an input value for size and it uses it to make a grid
        
        The values in the arrays are set to False by default, this means all the lights are off at the start'''
        self.size = s
        grid = [[False] * self.size for _ in range(self.size)]
        self.A = np.array(grid)
        
    def grid(self):
        '''calling this method returns the grid'''
        return self.A
    
    def count(self):
        '''calling this method counts the number of lights turned on (counting all the True values in the array)
        
        it returns the count for lights on'''
        lightsOnCount = np.count_nonzero(self.A)
        return lightsOnCount
        
    def turnOn(self, x1, y1, x2, y2): 
        '''this method turns the lights on according to the coordinate values given
        
        it returns the 2D array'''
        for row in range(y1, y2+1):
            for col in range(x1, x2+1):
                self.A[row][col]=True
        return self.A

    def turnOff(self, x1, y1, x2, y2):
        '''this method turns the lights off according to the coordinate values given
        
        it returns the 2D array'''
        for row in range(y1, y2+1):
            for col in range(x1, x2+1):
                self.A[row][col]=False
        return self.A


    def switch(self, x1, y1, x2, y2):
        '''this method switches the lights on to off and vice versa according to the coordinate values given.
        
        it returns the 2D array'''
        for row in range(y1, y2+1):
            for col in range(x1, x2+1):
                self.A[row][col]= not self.A[row][col]
        return self.A

