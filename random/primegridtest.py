from pandas import *

grid = [ [ 0, 1, 1, 0],
         [ 1, 0, 1, 0],
         [ 0, 0, 1, 0],
         [ 1, 0, 0, 0] ]

def rotate(gr):
    return list(zip(*gr[::-1]))

def bitand(gr1, gr2):
    return [x for x in y for y in gr1]

print('')
print(DataFrame(grid))
print('')
print(DataFrame(rotate(grid)))


