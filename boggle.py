import sys
import time
import math

#print(sys.argv[1])
# Get board from text fil and remove all spaces and newlines
boggleboard = open('sampleboard.txt', 'r')
boardtext = boggleboard.read()
boardtext = boardtext.replace(' ', '')
boardtext = boardtext.replace('\n', '')

# Find grid dimensions, cast to int
gridsize = (int)(math.sqrt(len(boardtext)))
print(gridsize)

# Create 2D array and populate with text
grid = [['' for i in range(gridsize)] for i in range(gridsize)]
for i in range(len(boardtext)):
    grid[i%4][i//4] = boardtext[i]

print(grid)

starttime = time.time()
elapsedtime = time.time() - starttime

#Begin writing output file
output = open('boggleout.txt', 'w')

output.write('Program #1: Fred Flinstone Problem-Solving\n')
output.write('Output of words found in boggle style: \n')

output.write('Elapsed time: ' + str(elapsedtime) + ' seconds')
