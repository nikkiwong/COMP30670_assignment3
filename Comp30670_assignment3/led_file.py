# where I will write the codes for the
class Lights:
    def __init__(self, s):
        self.size = s

    def create_grid(self):
        grid = [[0] * self.size for _ in range(self.size)]
        return grid


    def initial_light_status(self):
        pass

    def count(self):
        pass

    def turnOn(self):
        pass

    def turnOff(self):
        pass

    def switch(self):
        pass

# grid = Lights(10).create_grid()
#
# print(grid)


# grid = [[0] * 10 for _ in range(10)]
# print(grid)
