# CS470 Boggle solver
# Christopher Combs Spring 2017

import sys
import time
import math

# Start counting time and collect command line args
starttime = time.time()
dictfile = sys.argv[1]
boardfile = sys.argv[2]

# Read dictionary text file and populate the set
dictionary = open(dictfile, 'r')
wordset = frozenset(line.strip() for line in dictionary)

# Get board from text file and remove all spaces and newlines
boggleboard = open(boardfile, 'r')
boardtext = boggleboard.read()
boardtext = boardtext.replace(' ', '')
boardtext = boardtext.replace('\n', '')

# Find grid dimensions, cast to int
gridsize = (int)(math.sqrt(len(boardtext)))

# Create 2D array and populate with text
grid = [['' for i in range(gridsize)] for i in range(gridsize)]
for i in range(len(boardtext)):
    grid[i%4][i//4] = boardtext[i]

elapsedtime = time.time() - starttime

#Begin writing output file
output = open('boggleout.txt', 'w')

output.write('Program #1: Fred Flinstone Problem-Solving\n')
output.write('Output of words found in boggle style: \n')

output.write('Elapsed time: ' + str(elapsedtime) + ' seconds')
