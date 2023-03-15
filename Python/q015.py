# Starting in the top left corner of a 2×2 grid, and only being
# able to move to the right and down, there are exactly 6 routes
# to the bottom right corner.

# How many such routes are there through a 20×20 grid?

# equation : (2n)! / n! * n!

import math

grid = 20

def func(num):
    return math.factorial(2 * num) / (math.factorial(num) * math.factorial(num))

print(func(grid))