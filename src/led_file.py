import numpy as np

class Lights:
    def __init__(self, s):
        self.size = s
        self.grid = [[False] * self.size for _ in range(self.size)]

    def create_grid(self):
        self.grid = [[False] * self.size for _ in range(self.size)]
        self.A = np.array(self.grid)
        return self.A

    def initial_light_status(self):
        '''if we are reading from a new file then reset all values to boolean false or 0'''

    def count(self):
        # [row.count(True) for row in self.grid]
        lightsOnCount = sum(row.count(True) for row in self.grid)
        return lightsOnCount

    def get_coord(self):
        #will get the coords from the read_uri method. This is temporary method
        pass

    def turnOn(self):
        # coord=[x1,y1,x2,y2]
        # coord = [-2, 11, -4, 22]
        coord = get_coord()
        for i in range(len(coord)):
            if coord[i] < 0:
                coord[i] = 0
            elif coord[i] > len(self.grid):
                coord[i] = len(self.grid) - 1

        while coord[1] <= coord[3]:
            x = coord[0]
            while x <= coord[2]:
                self.A[coord[1]][x] = True
                x += 1
            coord[1] += 1
            
#         for row in range(y1, y2+1):
#             for col in range(x1, x2+1):
#                 self.grid[row][col]=True

    def turnOff(self):
        for i in self.A:
            for j in i:
                if j==True:
                    j=False




    def switch(self):
        pass

# grid = Lights(10).create_grid()
#
# print(grid)

# grid = [[0] * 10 for _ in range(10)]
print(Lights(10).create_grid())

def execute_command(self, cmd_str):
    #if the command is turn onthen run turn on method
    #else if command is turn off etc etc
def parse_cmd_str:
 #should take a string and figure out what the commands and coords are. 
 #returns cmd etc
 
 
 
 #turn on, turn off, switch in the order...