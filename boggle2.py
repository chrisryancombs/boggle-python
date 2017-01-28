# CS470 Boggle solver
# Christopher Combs Spring 2017

import sys
import time
import math

class coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def isvalid(self, gridsize):
        if self.x < 0 or self.y < 0:
            if self.x >= gridsize or self.y >= gridsize:
                return False
        return True

    def getadjacents(self, grid):
        adjacents = []
        for i in range(len(grid)):
            for j in range(len(grid)):
                test = coord(i,j)
                if test.isvalid(len(grid)) ==  True and test != self:
                    if (test.x == self.x + 1 or test.x == self.x or test.x == self.x - 1):
                        if (test.y == self.y + 1  or test.y == self.y or test.y == self.y - 1):
                            adjacents.append(test)
        return adjacents


def search(grid, dictionary):
    root = coord(1,2)
    word = grid[1][2]
    recsearch(root, word, grid, dictionary)
    return

def recsearch(current, word, grid, dictionary):
    word += grid[current.x][current.y]
    print(word)
    if word in dictionary:
        print(word)
    adjacents = current.getadjacents(grid)
    for i in range(len(adjacents)):
        if len(word) < 4:
            recsearch(adjacents[i], word, grid, dictionary)
    return

starttime = time.time()

# Read dictionary text file and populate the set
dictionary = open(sys.argv[1], 'r')
wordset = frozenset(line.strip() for line in dictionary)

# Get board from text file and remove all spaces and newlines
boggleboard = open(sys.argv[2], 'r')
boardtext = boggleboard.read().replace(' ', '').replace('\n', '')

# Find grid dimensions, cast to int
gridsize = (int)(math.sqrt(len(boardtext)))

# Create 2D array and populate with text
grid = [['' for i in range(gridsize)] for i in range(gridsize)]
for i in range(len(boardtext)):
    grid[i%4][i//4] = boardtext[i]

elapsedtime = time.time() - starttime

search(grid, wordset)
#Begin writing output file
output = open('boggleout.txt', 'w')

output.write('Program #1: Fred Flintstone Problem-Solving\n')
output.write('Output of words found in boggle style: \n')
output.write('Elapsed time: ' + str(elapsedtime) + ' seconds')
