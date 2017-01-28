# CS470 Boggle solver
# Christopher Combs Spring 2017

# This program takes in two command line arguments:
# the first is the name of the boggle board text file,
# and the second is the name of the dictionary text file.

import sys, time, math
def creategrid():
    # Get board from text file and put into 2D array
    boggleboard = open(sys.argv[2], 'r')
    boardtext = boggleboard.read().replace(' ', '').replace('\n', '')
    gridsize = (int)(math.sqrt(len(boardtext)))
    grid = [['' for i in range(gridsize)] for i in range(gridsize)]
    for i in range(len(boardtext)):
        grid[i%gridsize][i//gridsize] = boardtext[i]
    return grid

def createtrie():
    # Read dictionary text file and populate the trie
    dictionary = open(sys.argv[1], 'r')
    trie = dict()
    for word in (line.strip() for line in dictionary):
        word = word.replace('qu','q')
        current = trie
        for char in word:
            if char in current:
                current = current[char]
            else:
                current[char] = {}
                current = current[char]
        current['stop'] = 'stop'
    return trie

def intrie(searchword, dictionary):
    # Search for a word in the trie
    current = dictionary
    totalword = ''
    for letter in searchword:
        totalword += letter.lower()
        if letter in current:
            current = current[letter]
            if totalword == searchword and 'stop' in current:
                return 'word'
            elif totalword == searchword:
                return 'part'
    return False

def search(grid, dictionary):
    # Helper method for recursive search
    found = [[] for i in range(((len(grid))*(len(grid)))+1)]
    for i in range(len(grid)):
        for j in range(len(grid)):
            recsearch(i, j, '', [], grid, dictionary, found)
    return found

def recsearch(x, y, word, searched, grid, dictionary, found):
    # Recursively search boggle board
    word += grid[x][y]
    found[0].append('a')
    if intrie(word.lower(), dictionary) == 'word':
        found[len(word)].append(word)
    if intrie(word.lower(), dictionary) in ['part', 'word']:
        searched.append(str(x)+','+str(y))
        for i in range(len(grid)):
            for j in range(len(grid)):
                if i >= 0 and i < len(grid) and i >= (x-1) and i <= (x+1):
                    if j >= 0 and j < len(grid) and j >= (y-1) and j <= (y+1):
                        if ((i == x and j == y) == False) and ((str(i)+','+str(j)) not in searched):
                            recsearch(i, j, word, list(searched), grid, dictionary, found)

# Initialize by creating data structures and opening a file to write to
mytrie = createtrie()
mygrid = creategrid()
output = open('boggleout.txt', 'w')
starttime = time.time()
found = search(mygrid, mytrie)
elapsedtime = time.time() - starttime

#Begin writing output file
output.write('Program #1: Fred Flintstone Problem-Solving\n')
output.write('Christopher Combs CS470\n')
output.write(open(sys.argv[2], 'r').read())
allwords = []
for i in range(2, len(found)):
    if len(found[i]) > 0:
        output.write(str(i) + ' letter words: ')
        for word in list(set(found[i])):
            output.write(word + ", ")
        output.write('\n')
        allwords += found[i]
allwords.sort()
output.write('All words: ' + str(list(set(allwords))) + '\n')
output.write('Found ' + str(len(list(set(allwords)))) + ' words total\n')
output.write('Elapsed time: ' + str(elapsedtime) + ' seconds' + '\n')
output.write('Number of recursive searches: ' + str(len(found[0])))
