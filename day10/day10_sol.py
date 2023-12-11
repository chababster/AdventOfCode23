# AdventOfCode  Day 10
# Author        Chababster


# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
pipeList = {'|' : ['n','s'],
            '-' : ['e','w'],
            'L' : ['n','e'],
            'J' : ['n','w'],
            '7' : ['s','w'],
            'F' : ['s','e']}

# Open and read all lines from puzzle file
lines = []
with open('day10_puzzle.txt','r') as f:
    lines = f.read().splitlines()

for rowCount,line in enumerate(lines):
    for charCount,char in enumerate(line):
        if(char in "S"):
            # Create 3x3 square for the starting point
            # [] [] [] 
            # [] S  []
            # [] [] []
            line0="{}{}{}".format(lines[rowCount-1][charCount-1],
                                    lines[rowCount-1][charCount],
                                    lines[rowCount-1][charCount+1])
            line1="{}{}{}".format(lines[rowCount][charCount-1],
                                    char,
                                    lines[rowCount][charCount+1])
            line2="{}{}{}".format(lines[rowCount+1][charCount-1],
                                    lines[rowCount+1][charCount],
                                    lines[rowCount+1][charCount+1])
            
            if(line0[1] in pipeList.keys()):
                if('s' in pipeList[line0[1]]):
                    print(pipeList[line0[1]])

            if(line1[0] in pipeList.keys()):
                if(line1[0] == '-' or 'e' in pipeList[line1[1]][1]):
                    print(pipeList[line1[1]])
            