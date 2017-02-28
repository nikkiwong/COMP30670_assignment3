import numpy as np

class Lights:
    def __init__(self, s):
        self.size = s
        grid = [[False] * self.size for _ in range(self.size)]
        self.A = np.array(grid)
        
    def grid(self):
        return self.A
    
    def count(self):
        # [row.count(True) for row in self.grid]
        lightsOnCount = np.count_nonzero(self.A)
        return lightsOnCount
        
    def turnOn(self, x1, y1, x2, y2):
        for row in range(y1, y2+1):
            for col in range(x1, x2+1):
                self.A[row][col]=True
        return self.A

    def turnOff(self, x1, y1, x2, y2):
        for row in range(y1, y2+1):
            for col in range(x1, x2+1):
                self.A[row][col]=False
        return self.A


    def switch(self, x1, y1, x2, y2):
        for row in range(y1, y2+1):
            for col in range(x1, x2+1):
                self.A[row][col]= not self.A[row][col]
        return self.A

# grid = Lights(10).create_grid()
#
# print(grid)

# grid = [[0] * 10 for _ in range(10)]

def execute_command(self, cmd_str):
    pass
    #if the command is turn onthen run turn on method
    #else if command is turn off etc etc
#turn on, turn off, switch in the order...