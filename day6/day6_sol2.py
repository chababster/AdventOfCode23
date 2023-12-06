# AdventOfCode  Day 6
# Author        Chababster
# --- PT 2 --- 

# Import libs 
from progress.bar import Bar as pbar

# Open file and read
lines = []
with open('day6_puzzle.txt','r') as file:
    lines = file.read().splitlines()

# Split the time and distance strings into usable lists 
times = lines[0][5:].split()
dists = lines[1][10:].split()

# Piece together all the numbers into actual time and dists
timeActual = ""
for time in times:
    timeActual = timeActual + time

distActual = ""
for dist in dists:
    distActual = distActual + dist

# Convert the strings into ints
timeActual = int(timeActual)
distActual = int(distActual)

# Obj for storing the ways we can win
waysToWin = 0

# For 0 .. timeActual, calculate if we can potentially win, if so
# increment the counter
with pbar('Calculating...',max=timeActual) as bar:
    for timeHeld in range(timeActual):
        # If the current timeHeld ends up in a greater max distance 
        # we increment our waysToWin counter
        if ( ( (timeHeld) * (timeActual - timeHeld) ) > distActual ):
            waysToWin = waysToWin + 1
        bar.next()
# Print the ways to win
print(waysToWin)