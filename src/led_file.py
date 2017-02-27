import numpy as np

class Lights:
    def __init__(self, s):
        self.size = s
        grid = [[False] * self.size for _ in range(self.size)]
        self.A = np.array(grid)
        
    def count(self):
        # [row.count(True) for row in self.grid]
        lightsOnCount = np.count_nonzero(self.A)
        return lightsOnCount
        
    def turnOn(self, x1, y1, x2, y2):
        for row in range(y1, y2+1):
            for col in range(x1, x2+1):
                self.A[row][col]=True
        return self.A
        
        # coord=[x1,y1,x2,y2]
        # coord = [-2, 11, -4, 22]
#         coord = get_coord()
#         for i in range(len(coord)):
#             if coord[i] < 0:
#                 coord[i] = 0
#             elif coord[i] > len(self.grid):
#                 coord[i] = len(self.grid) - 1
# 
#         while coord[1] <= coord[3]:
#             x = coord[0]
#             while x <= coord[2]:
#                 self.A[coord[1]][x] = True
#                 x += 1
#             coord[1] += 1

    def turnOff(self, x1, y1, x2, y2):
        for row in range(y1, y2+1):
            for col in range(x1, x2+1):
                self.A[row][col]=False
        return self.A


    def switch(self):
        for i in range(0, len(self.A)):
            for j in range(0, len(self.A)):
                self.A[i][j]= not self.A[i][j]
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